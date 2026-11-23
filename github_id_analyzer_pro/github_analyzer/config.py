import os

APP_NAME = "GitHub ID Analyzer"
API_BASE_URL = "https://api.github.com"
CACHE_TTL_SECONDS = int(os.getenv("CACHE_TTL_SECONDS", "300"))
MAX_REPOSITORY_PAGES = 5
REPOSITORIES_PER_PAGE = 100
