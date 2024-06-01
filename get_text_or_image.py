
from get_random_text import get_random_text
from linebot.v3 import (
    WebhookHandler
)
from get_gif import get_gif
from linebot.v3.models import (
    TextSendMessage, ImageSendMessage
)
from linebot.v3.messaging import (
    Configuration,
    ApiClient,
    MessagingApi,
    ReplyMessageRequest,
)
import random
import os
from dotenv import load_dotenv

load_dotenv()

access_token = os.getenv("CHANNEL_ACCESS_TOKEN")
channel_secret = os.getenv("CHANNEL_SECRET")
configuration = Configuration(access_token=access_token)
handler = WebhookHandler(channel_secret)  


def reply_msg(message, reply_token):
    with ApiClient(configuration) as api_client:
        line_bot_api = MessagingApi(api_client)
        line_bot_api.reply_message_with_http_info(
            ReplyMessageRequest(
                messages=message,
                reply_token=reply_token,
            )
        )

def get_text_or_image(msg, token):
    try:
        if msg == 'itzy 想對我說...':
            result = get_random_text()
            reply_msg([TextSendMessage(text=result)],token)
        elif msg == '來張 GIPHY':
            image_urls = get_gif()
            random_url = random.choice(image_urls)
            reply_msg([TextSendMessage(text=f'隨機 gif 來囉：{random_url}')], token)
        elif msg == '椰咚' or msg == '禮志' or msg == 'yeji':
            img_url = 'https://res.cloudinary.com/dbrf4i0rb/image/upload/v1717041883/Screenshot_2024-05-30_at_08.33.37_zi7k7l.png'
            reply_msg( [ImageSendMessage(original_content_url=img_url, preview_image_url=img_url)], token)
        elif msg == 'Lia' or msg == '粒鴨' or msg == 'lia':
            img_url = 'https://res.cloudinary.com/dbrf4i0rb/image/upload/v1717052001/lia_hnwmmg.jpg'
            reply_msg( [ImageSendMessage(original_content_url=img_url, preview_image_url=img_url)], token)
        elif msg == '留真' or msg == '溜溜' or msg == 'ryujin':
            img_url = 'https://res.cloudinary.com/dbrf4i0rb/image/upload/v1717050660/phbvy5pm0dxk2kcedhzy.jpg'
            reply_msg( [ImageSendMessage(original_content_url=img_url, preview_image_url=img_url)], token)
        elif msg == '彩領' or msg == '教授' or msg == 'chaeryeong':
            img_url = 'https://res.cloudinary.com/dbrf4i0rb/image/upload/v1717051713/S__17547595_wwue5m.jpg'
            reply_msg( [ImageSendMessage(original_content_url=img_url, preview_image_url=img_url)], token)
        elif msg == '有娜' or msg == '芭比' or msg == 'yuna':
            img_url = 'https://res.cloudinary.com/dbrf4i0rb/image/upload/v1717051713/yuna_csimji.jpg'
            reply_msg( [ImageSendMessage(original_content_url=img_url, preview_image_url=img_url)], token)
        else:
            reply_msg( [TextSendMessage(text='🥲找不到相關圖片或GIF')])
    except:
        return 'error'
