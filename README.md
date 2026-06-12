# ⚽ FIFA World Cup 2026 — Outcome Prediction

> Poisson regression + Monte Carlo simulation to forecast every stage of the FIFA World Cup 2026 across 1,000 simulated tournaments.

**🔴 Live app → [montecarlos-fifa.streamlit.app](https://montecarlos-fifa.streamlit.app/)**

---

## What this does

Instead of gut feelings or pundit opinions, this project builds a data-driven forecasting pipeline that estimates each team's probability of reaching every stage of the 2026 tournament — from the Round of 32 all the way to lifting the trophy.

The short version: historical match data trains two Poisson regression models (one for home goals, one for away goals), those models power a match simulator, and that simulator runs the entire 48-team World Cup 1,000 times to produce stage-by-stage probabilities for every qualified nation.

---

## Result

| # | Team | Win probability |
|---|------|----------------|
| 🥇 | 🇪🇸 Spain | 26.9% |
| 🥈 | 🇦🇷 Argentina | 18.2% |
| 🥉 | 🇫🇷 France | 11.6% |
| 4 | 🏴󠁧󠁢󠁥󠁮󠁧󠁿 England | 6.9% |
| 5 | 🇧🇷 Brazil | 4.9% |
| 6 | 🇨🇴 Colombia | 4.1% |

Spain leads with the highest Elo rating in the dataset (2229) — the model consistently rewards historical dominance and recent form.

Full probability table across all 48 teams and all 6 stages is in `data/processed/wc2026_tournament_probabilities.csv`.

---

## Methodology

**1. Data collection & cleaning**
Historical international match results collected and cleaned — team name normalization, neutral venue handling, filtering low-signal friendlies.

**2. Elo ratings**
Custom Elo pipeline computes a dynamic strength score for every team before each match, updated after every result with recency and tournament-type weighting.

**3. Feature engineering**
Per-match features built from the Elo pipeline: home/away Elo, Elo delta, neutral venue flag, tournament importance weight, confederation encoding.

**4. Poisson regression (xG models)**
Two separate Poisson regression models trained — one predicting home goals, one predicting away goals. Poisson is the right distribution here: goals are count events with low expected values per 90 minutes.

**5. Match outcome probabilities**
Both models' expected goals are convolved across the Poisson distribution to get win, draw, and loss probabilities for any matchup.

**6. Tournament simulation**
Full 2026 bracket simulated: 12 groups, group standings, best third-place qualification, then knockout rounds (R32 → R16 → QF → SF → Final).

**7. Monte Carlo ×1,000**
The entire tournament is run 1,000 times. Each team's win probability = how often they won across all runs.

---

## Notebooks

| Notebook | What it does |
|----------|-------------|
| `0-data_fetch.ipynb` | Pulls raw match data |
| `1-data_cleaning.ipynb` | Cleans and normalizes |
| `2-feature_engineering_ELO.ipynb` | Builds Elo ratings |
| `3-feature_engineering_match_metadata.ipynb` | Engineers match features |
| `4-model_training.ipynb` | Trains Poisson models |
| `5-tournament_simulation.ipynb` | Runs Monte Carlo simulation |

---

## Streamlit app

Three views:

- **Probability explorer** — full 48-team ranking with win, final, SF, QF, R16, R32 probabilities
- **Live simulation** — simulate a full World Cup in real time with score-by-score reveals
- **Match explorer** — pick any two teams, get win/draw/loss odds, xG, Elo, form, H2H, and top scoreline probabilities

Run locally:
```bash
streamlit run simulation_app.py
```

---

## Stack

Python · Pandas · NumPy · SciPy · Statsmodels · Plotly · Streamlit · Jupyter · UV

---

## Acknowledgements

Inspired by and built upon the work of **Anas Riad**. Portions of the project structure were adapted from his World Cup prediction project.
