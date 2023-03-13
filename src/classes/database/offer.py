from mongoengine import *
from dotenv import load_dotenv
import os
from src.classes.offer import Offer
from time import strftime, localtime, sleep

# Script Setup
load_dotenv()

# Connecting to DB
connect(host=f'mongodb+srv://{os.getenv("mongodb_username")}:{os.getenv("mongodb_password")}@{os.getenv("mongodb_host")}/{os.getenv("mongodb_database")}?retryWrites=true&w=majority')

#Variables
db_requests = []

class MongoOffer(Document):
    raw_title = StringField(required=True)
    author = StringField(required=True)
    author_trades = IntField(required=True)
    post_id = StringField(required=True)
    body = StringField(required=True)
    post_time = DateTimeField(required=True)
    url = URLField(required=True)
    state = StringField(required=True)
    selling = StringField(required=True)
    buying = StringField(required=True)
    meta = {'collection': 'offers'}


def insert(offer: Offer) -> None:
    entry = MongoOffer()
    entry.raw_title = offer.raw_title
    entry.author = offer.author
    entry.author_trades = offer.author_trades
    entry.post_id = offer.id
    entry.body = offer.body
    entry.post_time = strftime('%Y-%m-%d %H:%M:%S', localtime(offer.post_time))
    entry.url = offer.url
    entry.state = offer.state
    entry.selling = offer.selling
    entry.buying = offer.buying
    entry.save()
    print(f"Inserted post {offer.id} into db.")
