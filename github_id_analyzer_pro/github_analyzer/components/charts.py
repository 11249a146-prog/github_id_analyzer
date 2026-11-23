import streamlit as st
import plotly.express as px
from github_analyzer.analytics.repository_analysis import language_counts, top_repositories, repository_totals

def render_overview_charts(df):
    left, right = st.columns(2)
    with left:
        st.subheader("Programming languages")
        languages = language_counts(df)
        if not languages.empty:
            fig = px.pie(languages, names="Language", values="Repositories", hole=.48)
            fig.update_layout(template="plotly_dark", margin=dict(t=15,b=15,l=10,r=10))
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("No language data is available.")
    with right:
        st.subheader("Repository types")
        totals = repository_totals(df)
        fig = px.bar(
            x=["Original", "Forked"], y=[totals["original"], totals["forked"]],
            labels={"x": "Repository type", "y": "Count"}, text_auto=True
        )
        fig.update_layout(template="plotly_dark", margin=dict(t=15,b=15,l=10,r=10))
        st.plotly_chart(fig, use_container_width=True)

    st.subheader("Top repositories by stars")
    top = top_repositories(df, "Stars", 10)
    if not top.empty:
        fig = px.bar(top.sort_values("Stars"), x="Stars", y="Name", orientation="h",
                     hover_data=["Language", "Forks", "Updated"])
        fig.update_layout(template="plotly_dark", yaxis_title="", margin=dict(t=10,b=10,l=10,r=10))
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No public repositories were returned.")
