import pandas as pd

def build_activity_dataframe(events):
    rows = []
    for event in events:
        rows.append({
            "Event": (event.get("type") or "Unknown").replace("Event", ""),
            "Repository": event.get("repo", {}).get("name", ""),
            "Created at (UTC)": event.get("created_at", ""),
            "Created date": (event.get("created_at") or "")[:10],
        })
    return pd.DataFrame(rows, columns=["Event", "Repository", "Created at (UTC)", "Created date"])

def event_counts(events_df):
    if events_df.empty:
        return pd.DataFrame(columns=["Event", "Count"])
    return events_df["Event"].value_counts().rename_axis("Event").reset_index(name="Count")
