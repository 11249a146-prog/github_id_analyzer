import streamlit as st
from github_analyzer.services.export_service import dataframe_to_csv, dataframe_to_excel

def render_repository_table(df, username):
    st.subheader("Repository explorer")
    if df.empty:
        st.info("No public repositories found.")
        return
    query = st.text_input("Search repository name or description", key="repo_search").lower()
    language_options = ["All"] + sorted(df["Language"].dropna().unique().tolist())
    language = st.selectbox("Filter by language", language_options)
    filtered = df
    if query:
        filtered = filtered[
            filtered["Name"].str.lower().str.contains(query, na=False)
            | filtered["Description"].str.lower().str.contains(query, na=False)
        ]
    if language != "All":
        filtered = filtered[filtered["Language"] == language]
    st.caption(f"Showing {len(filtered)} of {len(df)} repositories")
    st.dataframe(
        filtered[["Name", "Description", "Language", "Stars", "Forks", "Open issues", "Updated", "URL"]],
        use_container_width=True, hide_index=True,
        column_config={"URL": st.column_config.LinkColumn("Repository URL")}
    )
    a, b = st.columns(2)
    a.download_button("Download CSV", dataframe_to_csv(filtered),
                      f"{username}_repositories.csv", "text/csv", use_container_width=True)
    b.download_button("Download Excel", dataframe_to_excel(filtered),
                      f"{username}_repositories.xlsx",
                      "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                      use_container_width=True)
