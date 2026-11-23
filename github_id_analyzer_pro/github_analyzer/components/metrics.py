import streamlit as st
from github_analyzer.analytics.repository_analysis import repository_totals

def render_metrics(profile, df):
    totals = repository_totals(df)
    items = [
        ("Followers", profile.get("followers", 0)),
        ("Following", profile.get("following", 0)),
        ("Public repos", profile.get("public_repos", 0)),
        ("Stars received", totals["stars"]),
        ("Repository forks", totals["forks"]),
        ("Open issues", totals["issues"]),
    ]
    columns = st.columns(6)
    for column, (label, value) in zip(columns, items):
        column.metric(label, f"{int(value or 0):,}")
