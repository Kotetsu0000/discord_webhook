import os
import pytest
try:
    import dotenv
    dotenv.load_dotenv()
except ImportError:
    pass

from discord_webhook import DiscordWebhook

WEBHOOK_URL = os.getenv('WEBHOOK_URL')

def test_send():
    webhook = DiscordWebhook(WEBHOOK_URL, username='Test Bot', avatar_url='https://kotetsu0000.github.io/SIT_Coop_data/homeicon.png')
    webhook.send('Hello, World!\nThis is a test text message.')
    webhook.send('Hello, World!\nThis is a test message.', image_paths=['tests/test_image.png', 'tests/test_image.png'])
    webhook.send(image_paths=['tests/test_image.png', 'tests/test_image.png'])

if __name__ == '__main__':
    test_send()
