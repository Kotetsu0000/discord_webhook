import json
from urllib.request import Request, urlopen

class DiscordWebhook:
    def __init__(self, webhook_url:str) -> None:
        self.webhook_url = webhook_url

    def send(self, content, username=None, avatar_url=None):
        payload = {
            'content': content,
            'username': username,
            'avatar_url': avatar_url
        }

        headers = {
            'Content-Type': 'application/json'
        }

        request = Request(self.url, data=json.dumps(payload).encode(), headers=headers)
        urlopen(request)
