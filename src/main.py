# Libraries
import os
from dotenv import load_dotenv
from classes.reddit import Reddit
from classes.offer import Offer
from src.shared_methods import valid_title

# Script Setup
load_dotenv()

# Classes
reddit = Reddit(
    username=os.getenv("REDDIT_USERNAME"),
    password=os.getenv("REDDIT_PASSWORD"),
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET")
)


# for submission in reddit.api.subreddit("all").stream.submissions(skip_existing=True):
#     if valid_title(submission.title):
#         test = Offer(submission)
#         print(test)
#         print()

for submission in reddit.api.subreddit("hardwareswap").new(limit=100):
    if valid_title(submission.title):
        test = Offer(submission)
        print(test)
        print()
