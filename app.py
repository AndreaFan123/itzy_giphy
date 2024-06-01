from flask import Flask, request, abort

from linebot.v3 import (
    WebhookHandler
)
from linebot.v3.exceptions import (
    InvalidSignatureError
)
from linebot.v3.webhooks import (
    MessageEvent,
    TextMessageContent,
)
from get_text_or_image import get_text_or_image
from dotenv import load_dotenv
import os



load_dotenv()

channel_secret = os.getenv("CHANNEL_SECRET")
handler = WebhookHandler(channel_secret)

app = Flask(__name__)

def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        app.logger.info("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessageContent)
def handle_message(event):
    received_text = event.message.text
    received_token = event.reply_token
    get_text_or_image(received_text, received_token)


if __name__ == "__main__":
    app.run()

















