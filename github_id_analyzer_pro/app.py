import streamlit as st
from dotenv import load_dotenv
from github_analyzer.components.sidebar import render_sidebar
from github_analyzer.components.header import render_header
from github_analyzer.components.profile import render_profile
from github_analyzer.components.metrics import render_metrics
from github_analyzer.components.charts import render_overview_charts
from github_analyzer.components.repository_table import render_repository_table
from github_analyzer.components.activity import render_activity
from github_analyzer.services.github_service import GitHubService
from github_analyzer.analytics.repository_analysis import build_repository_dataframe
from github_analyzer.utils.errors import GitHubAPIError

load_dotenv()
st.set_page_config(page_title="GitHub ID Analyzer", page_icon="🐙", layout="wide")
render_header()

username, submitted = render_sidebar()
if submitted:
    if not username:
        st.sidebar.warning("Enter a GitHub username.")
    else:
        try:
            service = GitHubService()
            with st.spinner(f"Analyzing @{username}..."):
                profile = service.get_profile(username)
                repos = service.get_repositories(username)
                events = service.get_public_events(username)
            st.session_state["analysis"] = {
                "profile": profile, "repos": repos, "events": events,
                "username": username
            }
        except GitHubAPIError as exc:
            st.error(str(exc))
            st.session_state.pop("analysis", None)

data = st.session_state.get("analysis")
if not data:
    st.info("Enter a GitHub username in the sidebar and click **Analyze profile**.")
    st.markdown("### Explore public developer data")
    a, b, c = st.columns(3)
    a.markdown("**👤 Profile insights**\n\nAccount details, followers, following and public statistics.")
    b.markdown("**📦 Repository analytics**\n\nLanguages, stars, forks, issues and repository comparisons.")
    c.markdown("**⚡ Activity insights**\n\nRecent public events returned by GitHub.")
    st.caption("This app analyzes public GitHub data; it does not estimate a person's coding ability.")
else:
    profile, repos, events = data["profile"], data["repos"], data["events"]
    df = build_repository_dataframe(repos)
    render_profile(profile)
    render_metrics(profile, df)
    overview, repository_tab, activity_tab = st.tabs(
        ["📊 Overview", "📁 Repositories", "⚡ Activity"]
    )
    with overview:
        render_overview_charts(df)
    with repository_tab:
        render_repository_table(df, data["username"])
    with activity_tab:
        render_activity(events)
    st.caption("Data source: GitHub REST API · Results cached for five minutes.")
