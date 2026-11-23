from datetime import datetime, timezone

def account_age_years(created_at):
    if not created_at:
        return 0
    created = datetime.fromisoformat(created_at.replace("Z", "+00:00"))
    return max(0, round((datetime.now(timezone.utc) - created).days / 365.25, 1))

def profile_summary(profile, repository_count):
    return {
        "login": profile.get("login", ""),
        "name": profile.get("name") or profile.get("login", ""),
        "followers": int(profile.get("followers") or 0),
        "following": int(profile.get("following") or 0),
        "public_repositories": int(profile.get("public_repos") or repository_count),
        "account_age_years": account_age_years(profile.get("created_at")),
    }
