import json

import requests

class DiscordWebhook:
    def __init__(self, webhook_url:str, username=None, avatar_url=None) -> bool:
        self.webhook_url = webhook_url
        self.username = username
        self.avatar_url = avatar_url

    def send(self, text:str=None, image_paths:list=None) -> bool:
        if isinstance(image_paths, list):
            files = {}
            for i, image_path in enumerate(image_paths):
                extension = image_path.split(".")[-1]
                files[f'file{i}'] = (f"file{i}.png", open(image_path, "rb"), f"image/{extension}")
        else:
            files = None
                

        payload = {
            "username": self.username,
            "avatar_url": self.avatar_url,
            "content": text,
        }

        headers = {
            "User-Agent": "DiscordBot",
        }

        response = requests.post(self.webhook_url, headers=headers, data={"payload_json":json.dumps(payload)}, files=files)
        if isinstance(files, dict):
            for key, file in files.items():
                file[1].close()
        
        if response.status_code != 204:
            return False
        return True
