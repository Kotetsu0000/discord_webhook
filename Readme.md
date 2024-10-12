# discord_webhook

DiscordにWebhook経由でメッセージと画像を送信するためのシンプルなPythonライブラリです。

## インストール方法

pipを使用してインストールします。

```bash
pip install git+https://github.com/Kotetsu0000/discord_webhook.git
```

## 使い方

```python
from discord_webhook import DiscordWebhook

# Webhook URLを設定します。
webhook_url = "YOUR_WEBHOOK_URL"

# DiscordWebhookオブジェクトを作成します。
webhook = DiscordWebhook(webhook_url, username="Bot Name", avatar_url="https://example.com/avatar.png")

# メッセージを送信します。
webhook.send("Hello, world!")

# 画像付きのメッセージを送信します。
webhook.send("This is a message with images.", image_paths=["image1.png", "image2.jpg"])

# 画像のみを送信することも可能です。
webhook.send(image_paths=["image1.png", "image2.jpg"])
```

## 機能

- Webhook URL、ユーザー名、アバターURLの設定
- テキストメッセージの送信
- 画像の送信 (複数枚可)
- テキストと画像の同時送信

## APIリファレンス

### `DiscordWebhook(webhook_url: str, username=None, avatar_url=None)`

DiscordWebhookオブジェクトを初期化します。

- `webhook_url`: DiscordのWebhook URL。
- `username`: Webhookで使用するユーザー名。(オプション)
- `avatar_url`: Webhookで使用するアバター画像のURL。(オプション)

### `send(text: str = None, image_paths: list = None) -> bool`

メッセージを送信します。

- `text`: 送信するテキストメッセージ。(オプション)
- `image_paths`: 送信する画像のパスをリストで指定。(オプション)
- 戻り値: 送信に成功した場合は`True`、失敗した場合は`False`を返します。


```python
# 例：テキストと画像を送信
webhook.send("これはテストメッセージです。", image_paths=["path/to/image1.png", "path/to/image2.jpg"])

# 例：テキストのみを送信
webhook.send("これはテキストのみのメッセージです。")

# 例：画像のみを送信
webhook.send(image_paths=["path/to/image1.png", "path/to/image2.jpg"])
```
