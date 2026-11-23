import os
import requests
import streamlit as st
from github_analyzer.utils.errors import GitHubAPIError

API_ROOT = "https://api.github.com"

class GitHubService:
    def __init__(self):
        self.headers = {
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        }
        token = os.getenv("GITHUB_TOKEN", "").strip()
        if token:
            self.headers["Authorization"] = f"Bearer {token}"

    @st.cache_data(ttl=300, show_spinner=False)
    def _cached_get(_self, url, params=None):
        try:
            response = requests.get(url, headers=_self.headers, params=params, timeout=25)
        except requests.RequestException as exc:
            raise GitHubAPIError(f"Network error while contacting GitHub: {exc}") from exc
        if response.status_code == 404:
            raise GitHubAPIError("GitHub user or resource not found. Check the username.")
        if response.status_code == 403:
            reset = response.headers.get("X-RateLimit-Reset")
            extra = f" Rate limit reset epoch: {reset}." if reset else ""
            raise GitHubAPIError("GitHub API rate limit/access restriction reached." + extra +
                                 " Add a token in your local .env file to increase the limit.")
        if not response.ok:
            raise GitHubAPIError(f"GitHub API error {response.status_code}: {response.text[:300]}")
        return response.json()

    def get_profile(self, username):
        return self._cached_get(f"{API_ROOT}/users/{username}")

    def get_repositories(self, username):
        results = []
        for page in range(1, 6):
            batch = self._cached_get(
                f"{API_ROOT}/users/{username}/repos",
                {"per_page": 100, "page": page, "sort": "updated", "direction": "desc", "type": "owner"}
            )
            if not batch:
                break
            results.extend(batch)
            if len(batch) < 100:
                break
        return results

    def get_public_events(self, username):
        return self._cached_get(f"{API_ROOT}/users/{username}/events/public", {"per_page": 100})

    def get_rate_limit(self):
        return self._cached_get(f"{API_ROOT}/rate_limit")
