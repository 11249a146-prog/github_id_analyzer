import streamlit as st
st.set_page_config(page_title="How to use · GitHub ID Analyzer", page_icon="📘", layout="wide")
st.title("How to use")
st.markdown("""
1. Return to the main page.
2. Enter a GitHub username in the sidebar.
3. Select **Analyze profile**.
4. Explore Overview, Repositories and Activity tabs.
5. Filter repositories and export the visible results as CSV or Excel.

The app uses public GitHub endpoints. If you reach the unauthenticated rate limit, configure an optional token in a local `.env` file. Never commit that file.
""")
