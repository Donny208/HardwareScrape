import os
from dotenv import load_dotenv
import requests

# Script Setup
load_dotenv()

class Alerter:
    def __init__(self, chat_id, token):
        self.chat_id = chat_id
        self.token = token

    def send(self, msg:str):
        url = f'https://api.telegram.org/bot{self.token}/sendMessage'
        payload = {
            'chat_id': self.chat_id,
            'text': msg
        }
        requests.post(url, json=payload)
