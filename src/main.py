"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")

    # Starter example profile
    user_prefs = {"genre": "pop", "mood": "happy", "energy": 0.9, "valence": 0.5}
    user2_prefs = {"genre": "lofi", "mood": "chill", "energy": 0.3, "valence": 0.6}
    user3_prefs = {"genre": "metal", "mood": "angry", "energy": 0.95, "valence": 0.2}

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\n--- Top 5 Recommendations ---")
    print(f"Profile: genre={user_prefs['genre']}, mood={user_prefs['mood']}, "
          f"energy={user_prefs['energy']}, valence={user_prefs['valence']}\n")

    for rank, (song, score, explanation) in enumerate(recommendations, start=1):
        print(f"#{rank} {song['title']}")
        print(f"    Score      : {score:.2f} / 10")
        print(f"    Why        : {explanation}")
        print()


if __name__ == "__main__":
    main()
