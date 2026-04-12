---
name: Score Song Weighting — Option B
description: Current scoring weights in score_song() after Option B rebalance, saved as baseline before sensitivity testing
type: project
---

The `score_song()` function in `src/recommender.py` uses these weights (max total = 10.0):

| Signal  | Weight / Formula                          | Max pts |
|---------|-------------------------------------------|---------|
| Genre   | `+2.0` (binary match)                     | 2.0     |
| Mood    | `+2.5` (binary match)                     | 2.5     |
| Energy  | `3 × (1 - abs(user_energy - song_energy))`| 3.0     |
| Valence | `2.5 × (1 - abs(user_valence - song_valence))` | 2.5 |

**Why:** Previous weights (genre=4, mood=3, energy max=2, valence max=1) let a bare genre match outrank songs that were genuinely close in energy+valence. Option B rebalances so continuous features carry more weight.

**How to apply:** This is the agreed baseline before sensitivity testing. Any weight changes during testing should be compared against these values to evaluate improvement or regression.
