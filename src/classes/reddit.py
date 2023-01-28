import praw

class Reddit:
    def __init__(self, username, password, client_id, client_secret):
        self.api = praw.Reddit(
            user_agent="HardwareScrape",
            username=username,
            password=password,
            client_id=client_id,
            client_secret=client_secret
        )

    def get_username(self) -> str:
        return self.api.user.me()
