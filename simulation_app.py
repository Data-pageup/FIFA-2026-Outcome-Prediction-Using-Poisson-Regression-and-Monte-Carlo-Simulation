import streamlit as st

st.set_page_config(
    page_title="WC 2026 Predictor — Project Overview",
    page_icon="⚽",
    layout="wide",
)

# ── STYLES ──────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=JetBrains+Mono:wght@400;500&display=swap');

html, body, [data-testid="stAppViewContainer"] {
    background: #0C0C0C !important;
    color: #F0F0F0;
    font-family: 'Inter', sans-serif;
}
[data-testid="stHeader"] { background: transparent !important; }
[data-testid="stSidebar"] {
    background: #111 !important;
    border-right: 1px solid rgba(255,255,255,0.07);
}
[data-testid="stSidebar"] * { color: #aaa !important; }

/* remove default top padding */
.block-container { padding-top: 2.5rem !important; padding-bottom: 4rem !important; }

/* ── hero ── */
.hero-eyebrow {
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    color: #5DCAA5;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 1rem;
    display: flex;
    align-items: center;
    gap: 8px;
}
.hero-eyebrow::before {
    content: '';
    display: inline-block;
    width: 24px;
    height: 1px;
    background: #5DCAA5;
}
.hero-h1 {
    font-size: 3.2rem;
    font-weight: 300;
    line-height: 1.1;
    letter-spacing: -1.5px;
    color: #F0F0F0;
    margin-bottom: 1rem;
}
.hero-h1 strong { font-weight: 600; color: #fff; }
.hero-desc {
    font-size: 1rem;
    color: #888;
    font-weight: 300;
    line-height: 1.7;
    margin-bottom: 0;
    max-width: 580px;
}

/* ── stat boxes ── */
.stat-box {
    background: #141414;
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 12px;
    padding: 1.2rem 1.4rem;
    text-align: center;
}
.stat-num {
    font-family: 'JetBrains Mono', monospace;
    font-size: 2rem;
    font-weight: 500;
    color: #fff;
    line-height: 1;
}
.stat-lbl {
    font-size: 10px;
    color: #555;
    letter-spacing: 1px;
    text-transform: uppercase;
    margin-top: 6px;
}

/* ── section label ── */
.sec-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 10px;
    color: #555;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 0.5rem;
}
.sec-title {
    font-size: 1.5rem;
    font-weight: 400;
    letter-spacing: -0.4px;
    color: #fff;
    margin-bottom: 0.4rem;
}
.sec-sub {
    font-size: 0.9rem;
    color: #888;
    font-weight: 300;
    margin-bottom: 1.8rem;
}
.divider {
    height: 1px;
    background: rgba(255,255,255,0.07);
    margin: 2.5rem 0;
}

/* ── winner band ── */
.winner-band {
    background: linear-gradient(135deg, #0d2f24 0%, #0f3d2c 60%, #092820 100%);
    border: 1px solid rgba(29,158,117,0.35);
    border-radius: 16px;
    padding: 2.2rem 2.5rem;
    display: flex;
    align-items: center;
    gap: 2rem;
    margin-bottom: 1.5rem;
    position: relative;
    overflow: hidden;
}
.winner-tag {
    font-family: 'JetBrains Mono', monospace;
    font-size: 9px;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: #5DCAA5;
    margin-bottom: 6px;
    display: block;
}
.winner-name { font-size: 2rem; font-weight: 500; color: #fff; letter-spacing: -0.5px; margin-bottom: 4px; }
.winner-meta { font-size: 13px; color: rgba(93,202,165,0.65); }
.winner-prob {
    font-family: 'JetBrains Mono', monospace;
    font-size: 2.8rem;
    font-weight: 500;
    color: #5DCAA5;
    margin-left: auto;
    flex-shrink: 0;
}
.winner-prob small { font-size: 0.9rem; color: #1D9E75; margin-left: 3px; }

/* ── team rows ── */
.team-row {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 11px 16px;
    background: #141414;
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 10px;
    margin-bottom: 7px;
    transition: border-color 0.2s;
}
.team-row:hover { border-color: rgba(255,255,255,0.15); }
.t-rank { font-family: 'JetBrains Mono', monospace; font-size: 11px; color: #444; width: 18px; text-align: right; flex-shrink: 0; }
.t-flag { font-size: 18px; flex-shrink: 0; }
.t-name { font-size: 13px; font-weight: 500; color: #F0F0F0; width: 100px; flex-shrink: 0; }
.t-conf { font-size: 9px; padding: 2px 8px; border-radius: 20px; font-family: 'JetBrains Mono', monospace; letter-spacing: 0.5px; flex-shrink: 0; }
.t-track { flex: 1; height: 4px; background: rgba(255,255,255,0.06); border-radius: 2px; overflow: hidden; }
.t-fill { height: 100%; border-radius: 2px; }
.t-prob { font-family: 'JetBrains Mono', monospace; font-size: 13px; font-weight: 500; color: #F0F0F0; width: 38px; text-align: right; flex-shrink: 0; }

/* ── step rows ── */
.step {
    display: flex;
    gap: 18px;
    align-items: flex-start;
    padding: 1.4rem 0;
    border-bottom: 1px solid rgba(255,255,255,0.06);
}
.step:last-child { border-bottom: none; }
.step-icon {
    width: 40px; height: 40px;
    border-radius: 10px;
    display: flex; align-items: center; justify-content: center;
    font-size: 18px; flex-shrink: 0;
}
.step-title { font-size: 14px; font-weight: 500; color: #fff; margin-bottom: 4px; }
.step-desc { font-size: 12px; color: #888; line-height: 1.6; }
.step-tag {
    display: inline-block;
    font-family: 'JetBrains Mono', monospace;
    font-size: 9px;
    padding: 2px 8px;
    border-radius: 4px;
    border: 1px solid;
    margin-top: 8px;
}

/* ── pipe cards ── */
.pipe-card {
    background: #141414;
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 12px;
    padding: 1.2rem;
    height: 100%;
}
.pipe-icon { font-size: 20px; margin-bottom: 10px; display: block; }
.pipe-title { font-size: 13px; font-weight: 500; color: #fff; margin-bottom: 5px; }
.pipe-desc { font-size: 11px; color: #888; line-height: 1.5; }

/* ── tech chips ── */
.tech-row { display: flex; flex-wrap: wrap; gap: 8px; }
.tech-chip {
    font-size: 12px;
    padding: 6px 14px;
    border-radius: 8px;
    background: #141414;
    border: 1px solid rgba(255,255,255,0.08);
    color: #888;
}

/* ── footer ── */
.footer {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding-top: 2rem;
    border-top: 1px solid rgba(255,255,255,0.07);
    margin-top: 3rem;
    flex-wrap: wrap;
    gap: 1rem;
}
.footer-left { font-size: 12px; color: #444; }
.footer-badge {
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    padding: 5px 12px;
    border-radius: 6px;
    border: 1px solid rgba(29,158,117,0.3);
    color: #5DCAA5;
    background: rgba(29,158,117,0.06);
}
</style>
""", unsafe_allow_html=True)


# ── HERO ────────────────────────────────────────────────────────────────────
st.markdown('<div class="hero-eyebrow">FIFA World Cup 2026 — Forecasting Project</div>', unsafe_allow_html=True)
st.markdown("""
<div class="hero-h1">Predicting the<br><strong>World Cup winner</strong><br>with data.</div>
<p class="hero-desc">
Poisson regression trained on historical international match data, combined with Elo ratings
and Monte Carlo simulation to forecast every stage of the 2026 tournament across 1,000 full simulations.
</p>
""", unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ── HERO STATS ───────────────────────────────────────────────────────────────
c1, c2, c3, c4 = st.columns(4)
for col, num, lbl in [
    (c1, "1,000", "Simulated tournaments"),
    (c2, "48",    "Teams modeled"),
    (c3, "2",     "Poisson models"),
    (c4, "6",     "Tournament stages"),
]:
    with col:
        st.markdown(f"""
        <div class="stat-box">
            <div class="stat-num">{num}</div>
            <div class="stat-lbl">{lbl}</div>
        </div>""", unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)


# ── WINNER ───────────────────────────────────────────────────────────────────
st.markdown('<div class="sec-label">Simulation output</div>', unsafe_allow_html=True)
st.markdown('<div class="sec-title">Who wins the World Cup?</div>', unsafe_allow_html=True)
st.markdown('<div class="sec-sub">Based on 1,000 full Monte Carlo tournament runs. Win % = fraction of simulations where each team lifts the trophy.</div>', unsafe_allow_html=True)

st.markdown("""
<div class="winner-band">
    <div style="font-size:3rem; flex-shrink:0;">🏆</div>
    <div>
        <span class="winner-tag">Predicted champion</span>
        <div class="winner-name">🇫🇷 France</div>
        <div class="winner-meta">UEFA &nbsp;·&nbsp; Elo rank #1 &nbsp;·&nbsp; Consistent semi-final performer</div>
    </div>
    <div class="winner-prob">~21%<small>win prob</small></div>
</div>
""", unsafe_allow_html=True)

teams = [
    ("🇫🇷", "France",    "UEFA",     21, "#3D7EF0"),
    ("🇧🇷", "Brazil",    "CONMEBOL", 17, "#1D9E75"),
    ("🏴󠁧󠁢󠁥󠁮󠁧󠁿", "England",   "UEFA",     14, "#E24B4A"),
    ("🇦🇷", "Argentina", "CONMEBOL", 13, "#8B7EDD"),
    ("🇪🇸", "Spain",     "UEFA",     11, "#F0A030"),
    ("🇩🇪", "Germany",   "UEFA",      8, "#888888"),
    ("🇵🇹", "Portugal",  "UEFA",      6, "#1D9E75"),
    ("🇧🇪", "Belgium",   "UEFA",      4, "#E24B4A"),
]

conf_style = {
    "UEFA":     ("rgba(61,126,240,0.12)",  "#3D7EF0"),
    "CONMEBOL": ("rgba(29,158,117,0.12)", "#1D9E75"),
}

rows_html = ""
for i, (flag, name, conf, prob, color) in enumerate(teams):
    bg, tc = conf_style[conf]
    pct = round((prob / 21) * 100)
    rows_html += f"""
    <div class="team-row">
        <span class="t-rank">{i+1}</span>
        <span class="t-flag">{flag}</span>
        <span class="t-name">{name}</span>
        <span class="t-conf" style="background:{bg}; color:{tc}; border:1px solid {tc}30;">{conf}</span>
        <div class="t-track"><div class="t-fill" style="width:{pct}%; background:{color};"></div></div>
        <span class="t-prob">{prob}%</span>
    </div>"""

st.markdown(rows_html, unsafe_allow_html=True)
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)


# ── METHODOLOGY ──────────────────────────────────────────────────────────────
st.markdown('<div class="sec-label">Methodology</div>', unsafe_allow_html=True)
st.markdown('<div class="sec-title">How the model works</div>', unsafe_allow_html=True)
st.markdown('<div class="sec-sub">A six-stage pipeline from raw match data to tournament probability estimates.</div>', unsafe_allow_html=True)

steps = [
    ("📁", "#3D7EF0", "rgba(61,126,240,0.12)",
     "Data collection & cleaning",
     "Historical international match results gathered and cleaned — normalizing team names, handling neutral venues, filtering low-value friendlies.",
     "FOUNDATION"),
    ("📈", "#8B7EDD", "rgba(139,126,221,0.12)",
     "Elo rating engine",
     "Custom Elo pipeline built on all historical results with recency weighting and tournament-type adjustments. Gives every team a dynamic strength score before each match.",
     "TEAM STRENGTH"),
    ("⚙️", "#F0A030", "rgba(240,160,48,0.12)",
     "Feature engineering",
     "Match-level features constructed: home/away Elo, Elo delta, neutral venue flag, tournament importance weight, confederation encoding. These become model inputs.",
     "INPUT FEATURES"),
    ("∫", "#1D9E75", "rgba(29,158,117,0.12)",
     "Poisson regression — xG models",
     "Two separate Poisson regression models trained: one for home goals, one for away goals. Poisson is ideal because goals are count events with low expected values per match.",
     "STATISTICAL MODEL"),
    ("🎲", "#E24B4A", "rgba(226,75,74,0.12)",
     "Match outcome probabilities",
     "Expected goals from both models are convolved over the Poisson distribution to compute win, draw, and loss probabilities for every possible head-to-head matchup.",
     "PROBABILITY ENGINE"),
    ("🔁", "#5DCAA5", "rgba(93,202,165,0.12)",
     "Monte Carlo simulation ×1,000",
     "The entire 48-team World Cup — group stage, best third-place rules, R32, R16, QF, SF, Final — simulated 1,000 times. Stage-by-stage probabilities aggregated across all runs.",
     "MONTE CARLO"),
]

steps_html = ""
for emoji, color, bg, title, desc, tag in steps:
    steps_html += f"""
    <div class="step">
        <div class="step-icon" style="background:{bg}; font-size:20px;">{emoji}</div>
        <div style="flex:1;">
            <div class="step-title">{title}</div>
            <div class="step-desc">{desc}</div>
            <span class="step-tag" style="color:{color}; border-color:{color}40; background:{bg};">{tag}</span>
        </div>
    </div>"""

st.markdown(steps_html, unsafe_allow_html=True)
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)


# ── PIPELINE CARDS ────────────────────────────────────────────────────────────
st.markdown('<div class="sec-label">Prediction pipeline</div>', unsafe_allow_html=True)
st.markdown('<div class="sec-title">Core components</div>', unsafe_allow_html=True)
st.markdown('<div class="sec-sub">Each component feeds directly into the next, forming a coherent forecasting chain.</div>', unsafe_allow_html=True)

pipes = [
    ("📊", "#3D7EF0", "Historical match data",    "Cleaned CSV of international results going back decades"),
    ("📉", "#8B7EDD", "Elo ratings",              "Pre-match team strength scores updated after every result"),
    ("🔧", "#F0A030", "Feature matrix",           "Elo, venue, confederation, importance — engineered per match"),
    ("∫",  "#1D9E75", "xG Poisson models",        "Trained home + away goal expectation models"),
    ("↔️", "#E24B4A", "Outcome probabilities",    "Win / draw / loss odds for any head-to-head"),
    ("🏆", "#5DCAA5", "Tournament probabilities", "Monte Carlo win rates per stage, per team"),
]

cols = st.columns(3)
for i, (icon, color, title, desc) in enumerate(pipes):
    with cols[i % 3]:
        st.markdown(f"""
        <div class="pipe-card">
            <span class="pipe-icon" style="color:{color};">{icon}</span>
            <div class="pipe-title">{title}</div>
            <div class="pipe-desc">{desc}</div>
        </div>
        <div style="height:10px;"></div>
        """, unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)


# ── TECH STACK ────────────────────────────────────────────────────────────────
st.markdown('<div class="sec-label">Technologies</div>', unsafe_allow_html=True)
st.markdown('<div class="sec-title">Stack</div>', unsafe_allow_html=True)

techs = ["Python", "Statsmodels (Poisson)", "Pandas", "NumPy / SciPy", "Plotly", "Streamlit", "Jupyter", "UV package manager"]
chips = "".join(f'<span class="tech-chip">{t}</span>' for t in techs)
st.markdown(f'<div class="tech-row">{chips}</div>', unsafe_allow_html=True)


# ── FOOTER ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="footer">
    <div class="footer-left">FIFA World Cup 2026 Predictor &nbsp;·&nbsp; Monte Carlo + Poisson Regression</div>
    <div class="footer-badge">⚽ 48 teams · 1,000 simulations</div>
</div>
""", unsafe_allow_html=True)
