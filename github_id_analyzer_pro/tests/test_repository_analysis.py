from github_analyzer.analytics.repository_analysis import build_repository_dataframe, repository_totals, language_counts

def sample_repos():
    return [
        {"name": "alpha", "language": "Python", "stargazers_count": 5, "forks_count": 2,
         "open_issues_count": 1, "fork": False},
        {"name": "beta", "language": "JavaScript", "stargazers_count": 3, "forks_count": 1,
         "open_issues_count": 0, "fork": True},
    ]

def test_repository_totals():
    df = build_repository_dataframe(sample_repos())
    assert repository_totals(df) == {
        "stars": 8, "forks": 3, "issues": 1, "original": 1, "forked": 1
    }

def test_language_counts():
    df = build_repository_dataframe(sample_repos())
    assert set(language_counts(df)["Language"]) == {"Python", "JavaScript"}
