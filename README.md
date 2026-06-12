# FIFA 2026 Outcome Prediction Using Poisson Regression and Monte Carlo Simulation

## Overview

This project aims to predict the outcomes of the FIFA World Cup 2026 using a data-driven football analytics pipeline. Instead of relying on subjective rankings or expert opinions, the project combines historical international match data, Elo ratings, Poisson regression, and Monte Carlo simulation to estimate each team's probability of progressing through every stage of the tournament.

The overall workflow follows a structured approach:

1. Collect and clean historical international football match data.
2. Construct team strength ratings using Elo methodology.
3. Engineer match-level features that capture team quality and contextual factors.
4. Train statistical models to estimate expected goals for each team.
5. Convert expected goals into match outcome probabilities.
6. Simulate the entire World Cup thousands of times using Monte Carlo methods.
7. Aggregate simulation results to estimate the probability of reaching each tournament stage.

The result is a fully reproducible tournament forecasting system capable of estimating each nation's likelihood of reaching the Round of 32, Round of 16, Quarter-finals, Semi-finals, Final, and ultimately winning the FIFA World Cup 2026.

---

## Project Goal

The primary objective of this project is to estimate the probability of each qualified team reaching different stages of the FIFA World Cup 2026.

In addition to the prediction engine, an interactive Streamlit application was developed to:

* Explore tournament probabilities.
* Simulate an individual World Cup run in real time.
* Compare match-up probabilities between any two teams.
* Visualize tournament outcomes and progression paths.

---

## Methodology

### 1. Data Collection and Preparation

Historical international football match data was collected and cleaned to create a consistent dataset suitable for modeling.

Additional reference datasets were prepared, including:

* FIFA World Cup 2026 tournament structure.
* Group-stage fixtures.
* Knockout-stage bracket mappings.
* FIFA rankings.
* Confederation information.

### 2. Team Strength Estimation (Elo Ratings)

A custom Elo rating pipeline was built to estimate team strength before each match.

These ratings provide a dynamic measure of team quality based on historical performance and form.

### 3. Feature Engineering

Several match-level features were generated, including:

* Home team Elo rating
* Away team Elo rating
* Elo rating difference
* Neutral venue indicator
* Tournament importance weight
* Home confederation
* Away confederation

These features serve as inputs to the goal prediction models.

### 4. Goal Prediction Modeling

Two separate Poisson regression models were trained:

* Home-team goals model
* Away-team goals model

Poisson regression is widely used in football analytics because goals are count-based events and generally follow Poisson-like distributions.

The models estimate expected goals for both teams in a match.

### 5. Match Outcome Probabilities

Expected goals from the Poisson models are converted into probabilities for:

* Home win
* Draw
* Away win

These probabilities become the foundation for tournament simulation.

### 6. Tournament Simulation

The entire FIFA World Cup tournament structure was simulated, including:

* Group-stage matches
* Group standings
* Best third-placed qualification rules
* Round of 32
* Round of 16
* Quarter-finals
* Semi-finals
* Final

### 7. Monte Carlo Simulation

To estimate long-run tournament probabilities, the complete World Cup was simulated 1,000 times.

By repeating the tournament many times, the project estimates how frequently each team reaches each stage, providing a probabilistic forecast rather than a single deterministic prediction.

---

## Project Structure

```text
football_wc2026/
│
├── data/
│   ├── interim/
│   ├── processed/
│   ├── raw/
│   └── reference/
│
├── models/
│   ├── poisson_home.pkl
│   ├── poisson_away.pkl
│   └── feature_columns.pkl
│
├── notebooks/
│   ├── 0-data_fetch.ipynb
│   ├── 1-data_cleaning.ipynb
│   ├── 2-feature_engineering_ELO.ipynb
│   ├── 3-feature_engineering_match_metadata.ipynb
│   ├── 4-model_training.ipynb
│   └── 5-tournament_simulation.ipynb
│
├── src/
│   ├── data_loader.py
│   ├── prediction.py
│   ├── group_stage.py
│   ├── qualification.py
│   ├── bracket.py
│   ├── knockout.py
│   ├── tournament.py
│   └── styling.py
│
├── simulation_app.py
├── pyproject.toml
├── uv.lock
└── README.md
```

---

## Technologies Used

* Python
* Pandas
* NumPy
* SciPy
* Statsmodels
* Streamlit
* Jupyter Notebooks
* Matplotlib
* UV Package Manager

---

## Results

The final output is a probability table containing each team's likelihood of reaching:

* Round of 32
* Round of 16
* Quarter-finals
* Semi-finals
* Final
* Tournament Winner

Results are stored in:

```text
data/processed/wc2026_tournament_probabilities.csv
```

The Monte Carlo simulations indicated that teams with the strongest Elo ratings consistently achieved the highest tournament-winning probabilities.

---

## Streamlit Application

The interactive dashboard includes:

* Tournament probability explorer
* Single-run World Cup simulator
* Team-vs-team match probability explorer
* Tournament progression visualization

---

## Acknowledgements

This project was inspired by and built upon ideas from the work of **Anas Riad**. Portions of the project structure and methodology were adapted from his World Cup prediction project.

