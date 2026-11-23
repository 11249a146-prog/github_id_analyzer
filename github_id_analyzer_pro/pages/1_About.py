import streamlit as st
st.set_page_config(page_title="About · GitHub ID Analyzer", page_icon="ℹ️", layout="wide")
st.title("About GitHub ID Analyzer")
st.write(
    "GitHub ID Analyzer is a learning project that visualizes public GitHub profile, "
    "repository and recent public-event data using the GitHub REST API."
)
st.subheader("What the metrics mean")
st.markdown("""
- **Followers / Following:** public account relationship counts.
- **Stars:** stars received by repositories owned by the account.
- **Forks:** forks reported on those repositories.
- **Open issues:** open issues reported by the repository API.
- **Languages:** primary language field reported for each repository.
- **Public events:** a limited set of recent public events from GitHub.
""")
st.warning("These metrics do not measure programming skill, code quality, private work, or employability.")
