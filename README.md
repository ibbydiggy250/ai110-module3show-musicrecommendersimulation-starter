# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Explain your design in plain language.

Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
- What information does your `UserProfile` store
- How does your `Recommender` compute a score for each song
- How do you choose which songs to recommend

You can include a simple diagram or bullet list if helpful.

 Real recommendation systems aren't just a black and white sorting algorithm. Instead, it takes a lot of considerations, such as user preferences, popularity, genre, etc. It employs both a scoring and ranking system to not only get the matching number for the song, but also rank it based on factors such as alphabetically, relevance, popularity, etc. This is mostly content based filtering, where a user is given a recommendation based on the actual content, rather than widespread popularity. My version will prioritize energy, genre, mood and valence, as these are emotional states and preferences that is personal to the user.

 From Song and UserProfile we can implement the energy, valence, genre and mood features from the Song object, and the target_energy, favorite_genre and favorite_mood features from the UserProfile class. We will ignore the likes_acoustic, as a boolean is weak when it comes to preference.

 My finalized Algorithm recipe will be ranking based on genre, mood, energy, and valence. Since we need to score songs based on metrics, we will weigh each of these things seperately. Genre will be 4 points, mood will be 3 points, energy will be 2 points, and valence will be 1 point, for a total of 10. Most people resonate with genre the most, so it seems to be the best attribute to prioritize. However, while it is an important attribute, a genre still has a wide variety of songs and moods, and something in the genre may be less impactful than something outside the genre but with a similar mood. This bias will exist, but for general purposes, genre seems to be the best priority.
---

## Screenshot of Output:
![alt text](image.png)
---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

User preference "genre": "pop", "mood": "sad", "energy": 0.8, "valence": 0.2:
![alt text](image-1.png)
User preference "genre": "lofi", "mood": "chill", "energy": 0.3, "valence": 0.6:
![alt text](image-2.png)
User preference "genre": "metal", "mood": "angry", "energy": 0.95, "valence": 0.2:
![alt text](image-3.png)


I then experimented to see the effect of weighting.
With normal weights: Profile: genre=pop, mood=angry, energy=0.2, valence=0.5
![alt text](image-4.png)

With a doubling of energy and halving of genre:
![alt text](image-5.png)

The second option wa sa lot worse, as Iron Descent was the only "angry" music, and a person with an angry profile getting Moonlit Sonata which is sad is completely off.
---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this


---

## 7. `model_card_template.md`

Combines reflection and model card framing from the Module 3 guidance. :contentReference[oaicite:2]{index=2}  

```markdown
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

Recommender systems work on multiple different factors. User based recommenders especially take attributes of your profile to give you recommendations that would best match your tastes. While our recommender was rudimentary here, real recommenders take thousands of datapoints with many more attributes in order to give the best results. Something interesting I learned is how important the weighting was. I thought that even though genre was my strongest weight originally, other choices would sitll go to first if the mood or energy matched. Instead, the same song always appeared first, because genre was too heavy of a weighting. After redistributing it, I got a lot better results that matched my intuition. Based on this, I learned that I can tailor recommendations by just changing what I listen to. The more I listen to metal music for example, I will get metal recommendations. These apps match the results based on your recent profile flavor, so switching it around can give you different recommendations. In this project, I used AI a lot when planning my flavor profile. I had it help me make the scoring equations, what attributes I should use, with me overseeing it. AI suggested some attributes that I rejected, and used some weightings which I didn't like. Overall, AI helped me plan and code this project, making it a lot more efficient.


