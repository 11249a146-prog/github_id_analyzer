import streamlit as st
from github_analyzer.analytics.profile_analysis import account_age_years

def render_profile(profile):
    left, right = st.columns([1, 5])
    with left:
        avatar = profile.get("avatar_url")
        if avatar:
            st.image(avatar, width=145)
    with right:
        st.subheader(profile.get("name") or profile.get("login"))
        st.markdown(f"**[@{profile.get('login')}]({profile.get('html_url')})**")
        st.write(profile.get("bio") or "No public bio provided.")
        details = [profile.get("company"), profile.get("location"), profile.get("blog")]
        st.caption(" · ".join(str(x) for x in details if x) or "No additional public profile details")
        age = account_age_years(profile.get("created_at"))
        st.caption(f"GitHub member for approximately {age} years · Joined {(profile.get('created_at') or '')[:10]}")
