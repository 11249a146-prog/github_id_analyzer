import streamlit as st

def render_sidebar():
    with st.sidebar:
        st.header("🔎 Analyze a profile")
        username = st.text_input("GitHub username", placeholder="e.g. torvalds").strip()
        submitted = st.button("Analyze profile", type="primary", use_container_width=True)
        st.divider()
        st.markdown("**Analysis includes**")
        st.caption("Profile · Repositories · Languages · Stars · Forks · Public events")
        st.markdown("**API access**")
        st.caption("Public data works without a token. A local token raises the API rate limit.")
        st.caption("Never commit your `.env` file.")
    return username, submitted
