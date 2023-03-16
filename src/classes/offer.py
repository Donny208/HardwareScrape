import json
import datetime
from praw.models import Submission
from src.shared_methods import *



class Offer:
    def __init__(self, post: Submission):
        # Data from post
        self.raw_title = post.title
        self.author = post.author.name
        self.author_trades = re.sub(r'\D', '', post.author_flair_text) if post.author_flair_text else '0'
        self.id = post.id
        self.body = post.selftext
        self.post_time = post.created
        self.url = post.url

        # Data from text cleanup
        trades = get_trade(self.raw_title)
        self.state = get_state(self.raw_title).upper()
        self.selling = trades[0]
        self.buying = trades[1]
        self.on_alert_list = self.check_alert_list(self.selling)

    def check_alert_list(self, item: str) -> bool:
        with open("./src/resources/filter.json", 'r') as file:
            data = json.load(file)
            for alert in data['alerts']:
                if re.search(f".*{alert}.*", item):
                    return True
        return False

    def format_for_telegram(self):
        output = f"{self.author}({self.author_trades} trades) @ {self.state}\n" \
                 f"Selling: {self.selling}\n" \
                 f"Wants: {self.buying}\n" \
                 f"URL: {self.url}\n" \
                 f"Created: {datetime.datetime.fromtimestamp(self.post_time)} MST"
        return output

    def __str__(self):
        output = f"{self.author}({self.author_trades} trades) @ {self.state}\n" \
                 f"Selling: {self.selling}\n" \
                 f"Wants: {self.buying}\n" \
                 f"Alert: {self.on_alert_list}\n" \
                 f"Created: {datetime.datetime.fromtimestamp(self.post_time)} MST"
        return output
