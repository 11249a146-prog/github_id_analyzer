import pandas as pd

def build_repository_dataframe(repositories):
    rows = []
    for repo in repositories:
        rows.append({
            "Name": repo.get("name", ""),
            "Description": repo.get("description") or "",
            "Language": repo.get("language") or "Not specified",
            "Stars": int(repo.get("stargazers_count") or 0),
            "Forks": int(repo.get("forks_count") or 0),
            "Open issues": int(repo.get("open_issues_count") or 0),
            "Size (KB)": int(repo.get("size") or 0),
            "Updated": (repo.get("updated_at") or "")[:10],
            "Created": (repo.get("created_at") or "")[:10],
            "URL": repo.get("html_url", ""),
            "Is fork": bool(repo.get("fork", False)),
            "Archived": bool(repo.get("archived", False)),
            "Default branch": repo.get("default_branch", ""),
        })
    return pd.DataFrame(rows, columns=[
        "Name", "Description", "Language", "Stars", "Forks", "Open issues",
        "Size (KB)", "Updated", "Created", "URL", "Is fork", "Archived",
        "Default branch"
    ])

def repository_totals(df):
    if df.empty:
        return {"stars": 0, "forks": 0, "issues": 0, "original": 0, "forked": 0}
    return {
        "stars": int(df["Stars"].sum()),
        "forks": int(df["Forks"].sum()),
        "issues": int(df["Open issues"].sum()),
        "original": int((~df["Is fork"]).sum()),
        "forked": int(df["Is fork"].sum()),
    }

def language_counts(df):
    if df.empty:
        return pd.DataFrame(columns=["Language", "Repositories"])
    result = df[df["Language"] != "Not specified"]["Language"].value_counts()
    return result.rename_axis("Language").reset_index(name="Repositories")

def top_repositories(df, metric="Stars", limit=10):
    if df.empty or metric not in df.columns:
        return df.head(0)
    return df.sort_values(metric, ascending=False).head(limit)
