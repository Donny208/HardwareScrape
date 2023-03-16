# Libraries
import os
import atexit
from dotenv import load_dotenv
from src.classes.reddit import Reddit
from src.classes.alert import Alerter
from src.classes.offer import Offer
from src.classes.database.offer import insert
from src.shared_methods import valid_title


# Methods
def exit_handler():
    alert.send("Program Stopped.")


# Script Setup
load_dotenv()
atexit.register(exit_handler)

# Classes
reddit = Reddit(
    username=os.getenv("REDDIT_USERNAME"),
    password=os.getenv("REDDIT_PASSWORD"),
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET")
)

alert = Alerter(
    chat_id=os.getenv("TELEGRAM_CHAT_ID"),
    token=os.getenv("TELEGRAM_TOKEN")
)

alert.send("Program Started.")


for submission in reddit.api.subreddit("hardwareswap").stream.submissions(skip_existing=True):
    if valid_title(submission.title):
        offer = Offer(submission)

        if offer.on_alert_list:
            alert.send(offer.format_for_telegram())

        # Saving deal to database
        insert(offer)


# for submission in reddit.api.subreddit("hardwareswap").new(limit=1):
#     if valid_title(submission.title):
#         offer = Offer(submission)
#
#         # Sending out reminder if deal exists
#         if offer.on_alert_list:
#             alert.send(offer.format_for_telegram())
#
#         # Saving deal to database
#         insert(offer)
