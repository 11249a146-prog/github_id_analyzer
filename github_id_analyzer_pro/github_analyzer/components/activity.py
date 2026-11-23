import streamlit as st
import plotly.express as px
from github_analyzer.analytics.activity_analysis import build_activity_dataframe, event_counts

def render_activity(events):
    st.subheader("Recent public GitHub activity")
    df = build_activity_dataframe(events)
    if df.empty:
        st.info("No recent public events were returned.")
        return
    left, right = st.columns([1, 1.5])
    with left:
        counts = event_counts(df)
        fig = px.bar(counts.head(10), x="Count", y="Event", orientation="h")
        fig.update_layout(template="plotly_dark", margin=dict(t=10,b=10,l=10,r=10))
        st.plotly_chart(fig, use_container_width=True)
    with right:
        st.dataframe(df, use_container_width=True, hide_index=True)
    st.caption("GitHub's public events endpoint is limited and is not a complete contribution history.")
