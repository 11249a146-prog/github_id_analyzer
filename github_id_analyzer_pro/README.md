# GitHub ID Analyzer Pro

A modular Streamlit dashboard for exploring public GitHub profiles, repositories, languages, stars, forks, issues and recent public events.

## Main features
- Profile information and account age
- Follower, following and public repository metrics
- Repository analytics and language distribution
- Original vs. forked repository comparison
- Top repositories by stars
- Repository search and language filter
- CSV and Excel export
- Recent public event summary
- API response caching and readable error handling
- Modular source structure and unit tests

## Requirements
Python 3.10+ and an internet connection.

## Run on Windows PowerShell

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python -m streamlit run app.py
```

If script activation is blocked in PowerShell, run:
`Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`
Then activate the environment again.

Open the local URL printed by Streamlit (normally http://localhost:8501).

## Optional GitHub token
Unauthenticated public API requests have a low rate limit. To increase it:
1. Copy `.env.example` to `.env`.
2. Add your token after `GITHUB_TOKEN=`.
3. Restart Streamlit.

Use the minimum required permissions. Never paste tokens into source code, commit history, screenshots, or chat. `.env` is ignored by Git.

## Run tests
```powershell
pytest
```

## Project layout
- `app.py`: application entry point
- `github_analyzer/services`: GitHub API and export services
- `github_analyzer/analytics`: repository, activity and profile calculations
- `github_analyzer/components`: reusable Streamlit UI components
- `github_analyzer/utils`: validation, formatting and errors
- `pages`: About and usage pages
- `tests`: basic unit tests

## API endpoints
Uses GitHub's public REST API for user profiles, repositories, public events and rate-limit information.

## Limitations
Only public data is analyzed. The public events endpoint returns a limited recent-event window, not complete contribution history. Repository counts, stars and languages are not a direct measure of developer skill or code quality.
