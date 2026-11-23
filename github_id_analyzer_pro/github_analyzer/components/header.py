import streamlit as st

def render_header():
    st.markdown("""
    <style>
    .block-container{padding-top:1.8rem;max-width:1450px}
    .hero{padding:1.5rem 1.7rem;border-radius:18px;
      background:linear-gradient(115deg,#172554,#312e81);
      border:1px solid #394875;margin-bottom:1.2rem}
    .hero h1{color:white;margin:0;font-size:2.25rem}
    .hero p{color:#c7d2fe;margin:.45rem 0 0}
    </style>
    <div class="hero"><h1>🐙 GitHub ID Analyzer</h1>
    <p>Public profile intelligence, repository analytics and developer activity explorer.</p></div>
    """, unsafe_allow_html=True)
