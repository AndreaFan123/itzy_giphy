from flask import Flask, request, abort

from linebot.v3 import (
    WebhookHandler
)
from linebot.v3.exceptions import (
    InvalidSignatureError
)
from linebot.v3.messaging import (
    Configuration,
    ApiClient,
    MessagingApi,
    ReplyMessageRequest,
    TextMessage,
    ImageMessage
)
from linebot.v3.webhooks import (
    MessageEvent,
    TextMessageContent
)
from get_random_text import get_random_text
from get_gif import get_gif
from dotenv import load_dotenv
import os
import random


load_dotenv()

access_token = os.getenv("CHANNEL_ACCESS_TOKEN")
channel_secret = os.getenv("CHANNEL_SECRET")
configuration = Configuration(access_token=access_token)
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
    
    if received_text == '來張 gif':
        with ApiClient(configuration) as api_client:
            line_bot_api = MessagingApi(api_client)
            line_bot_api.reply_message_with_http_info(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text=reply_text)]
                )
            )
    else:
        image_urls = get_gif()
        random_url = random.choice(image_urls)
        with ApiClient(configuration) as api_client:
            line_bot_api = MessagingApi(api_client)
            line_bot_api.reply_message_with_http_info(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text=f'隨機 gif 來囉：{random_url}')]
                )
            )
    if received_text == 'itzy 想對我說...':
        random_lyrics = get_random_text()
        with ApiClient(configuration) as api_client:
            line_bot_api = MessagingApi(api_client)
            line_bot_api.reply_message_with_http_info(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text=random_lyrics)]
                )
            )
    if received_text == '椰咚' or received_text == '禮志' or received_text == 'yeji':
        img_url = 'https://res.cloudinary.com/dbrf4i0rb/image/upload/v1717041883/Screenshot_2024-05-30_at_08.33.37_zi7k7l.png'
        with ApiClient(configuration) as api_client:
            line_bot_api = MessagingApi(api_client)
            line_bot_api.reply_message_with_http_info(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[ImageMessage(original_content_url=img_url, preview_image_url=img_url)]
                )
            )
    elif received_text == 'Lia' or received_text == '粒鴨' or received_text == 'lia':
        img_url = 'https://res.cloudinary.com/dbrf4i0rb/image/upload/v1717052001/lia_hnwmmg.jpg'
        with ApiClient(configuration) as api_client:
            line_bot_api = MessagingApi(api_client)
            line_bot_api.reply_message_with_http_info(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[ImageMessage(original_content_url=img_url, preview_image_url=img_url)]
                )
            )
    elif received_text == '留真' or received_text == '溜溜' or received_text == 'ryujin':
        img_url = 'https://res.cloudinary.com/dbrf4i0rb/image/upload/v1717050660/phbvy5pm0dxk2kcedhzy.jpg'
        with ApiClient(configuration) as api_client:
            line_bot_api = MessagingApi(api_client)
            line_bot_api.reply_message_with_http_info(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[ImageMessage(original_content_url=img_url, preview_image_url=img_url)]
                )
            )
    elif received_text == '彩領' or received_text == '教授' or received_text == 'chaeryeong':
        img_url = 'https://res.cloudinary.com/dbrf4i0rb/image/upload/v1717051713/S__17547595_wwue5m.jpg'
        with ApiClient(configuration) as api_client:
            line_bot_api = MessagingApi(api_client)
            line_bot_api.reply_message_with_http_info(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[ImageMessage(original_content_url=img_url, preview_image_url=img_url)]
                )
            )
    elif received_text == '有娜' or received_text == '芭比' or received_text == 'yuna':
        img_url = 'https://res.cloudinary.com/dbrf4i0rb/image/upload/v1717051713/S__17547595_wwue5m.jpg'
        with ApiClient(configuration) as api_client:
            line_bot_api = MessagingApi(api_client)
            line_bot_api.reply_message_with_http_info(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[ImageMessage(original_content_url=img_url, preview_image_url=img_url)]
                )
            )
    else:
        reply_text = '找不到相關圖片或 gif'
        with ApiClient(configuration) as api_client:
            line_bot_api = MessagingApi(api_client)
            line_bot_api.reply_message_with_http_info(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text=reply_text)]
                )
            )


if __name__ == "__main__":
    app.run()

















