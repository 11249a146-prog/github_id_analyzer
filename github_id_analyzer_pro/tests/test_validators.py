from github_analyzer.utils.validators import valid_github_username

def test_valid_usernames():
    assert valid_github_username("octocat")
    assert valid_github_username("my-user-123")

def test_invalid_usernames():
    assert not valid_github_username("")
    assert not valid_github_username("-bad")
    assert not valid_github_username("bad-")
    assert not valid_github_username("has space")
