# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

EnergyMatcher
---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

 This recommender is a song recommender, that gives you songs based on different attributes such as genre, mood, energy, and valence. Based on your profile, a song will be matched based on these attributes. This recommender makes the assumption that every user cares about the same attributes equally, and does a one size fits all scoring system. It also assumes that the person only likes one type of genre and mood, and will only listen to that type. Because of these things, this recommender is more for classroom exploration rather than real use. To scale it more, we would have to add different parameters, more song choices, and tailor it to the user specifically. 
---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

In the scoring process, we only use the genre, mood, energy, and valence attributes. The other attributes don't seem like ones that would effectively match the energy of the user. The user inputs what genre they like, the mood they want, and the level of energy and valence they like. The genre and mood are scored on a direct match. If the genre matches exactly what the user picked, it gets full points, otherwise none. Same idea with mood. The genre has a +2 weighting, while the mood has a +2.5 weighting. Energy and valence are then judged based on how close they are to the users preference. These are not exact matches, rather they are proximity matches. Energy has a +3 weighting, and valence has a +2.5 weighting. Originally, I had a +4 for genre, +3 for mood, +2 for energy, and +1 for valence. However, after trying it out with different settings, I kept getting the same song in 1st place. This is when I knew genre was weighed too heavily, and changed it around.
---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

There are 18 songs, with genres such as pop, lofi, rock, ambient jazz, synthwave, indie pop, hip-hop, classical, country, metal, r&b, edm and the blue. The moods included are happy chill, intense, relaxed, focused, moody, motivated, melancholic, nostalgic, angry, romanstic, peaceful, and euphoric. This is a wide range of data, with examples from many different genres and moods in order to acommodate different tastes. The original dataset had 10 songs only. I added 8 more to cover different moods and genres that weren't in the original model. Parts of musical tastes are missing. First, there is not a lot of variation in the genre. In the dataset, there is roughly only one song for each genre type, which limits the suggestions for people with more niche genres. Also, moods such as sad and dreamy aren't in the data, which are pretty prevelant moods. Overall, this dataset is small, and was used mostly for testing rather than a wide demographic usage.

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

 The recommender is especially strong with the user profiles that are more represented in the datset. With genres such as pop and lofi, there are stronger matches, because there are more genre matches. However, it still works with other profiles pretty well because genre is not the strongest weight. The strongest pattern my recommender captures is the energy and valence. Since these aren't exact matches, I am able to get a wider net of songs that could match the users taste, which is especially strong when the genre and mood doesn't match. With the lofi and metal, the recommendation matched my intuition, as the lofi profile got low energy and chill music, while the metal profile had high energy and angry songs. 
---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

    While I tried to include the most relevant attributes of songs, there are still limitations to be discussed, both in the calculations and the dataset. In the dataset, the most favored songs are lofi and pop, since they come up the most. The rest of the genres only appear once. That means someone who likes a genre like metal will only recieve one metal song, versus someone who likes lofi will get multiple different songs. This is just the product of a small dataset. Another thing is that since we are treating genres and moods as binary, similar genres and moods will be ignored entirely. For example, if we compare metal with rock, they are actually very similar in terms of musical pallette, but the recommender will weigh it as 0, since it doesnt directly match metal. This will cause songs that the user still might like to be completely ignored.
---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

    I tested users who like pop, metal, and lofi. They seemed to be at different parts of the music spectrum, so it would be interesting to see how their music tastes line up. A person who likes metal usually had songs with a higher energy and lower valence, while a person who likes pop got the opposite. However, I also tested a person who likes pop, but with an angry mood and low energy. These results gave me something closer to the metal profile, showing a clear bias not based on genre. Lofi users usually got a lower energy and higher valence profile. Each profile had a unique taste, showing that the model can accurately differentiate between different flavor profiles.
---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

 To improve this model, the first thing I would do is add more data. I want more representation across genres, moods, energy levels, and other things. This allows me to better show users songs that would fit them, rather than only show one good song, and the rest be bad choices. 
---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  

Recommender systems work on multiple different factors. User based recommenders especially take attributes of your profile to give you recommendations that would best match your tastes. While our recommender was rudimentary here, real recommenders take thousands of datapoints with many more attributes in order to give the best results. Something interesting I learned is how important the weighting was. I thought that even though genre was my strongest weight originally, other choices would sitll go to first if the mood or energy matched. Instead, the same song always appeared first, because genre was too heavy of a weighting. After redistributing it, I got a lot better results that matched my intuition. Based on this, I learned that I can tailor recommendations by just changing what I listen to. The more I listen to metal music for example, I will get metal recommendations. These apps match the results based on your recent profile flavor, so switching it around can give you different recommendations.
