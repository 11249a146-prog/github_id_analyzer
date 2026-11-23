import re

USERNAME_PATTERN = re.compile(r"^[A-Za-z0-9](?:[A-Za-z0-9-]{0,37}[A-Za-z0-9])?$")

def valid_github_username(username):
    return bool(USERNAME_PATTERN.fullmatch((username or "").strip()))
