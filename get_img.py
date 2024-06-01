from linebot import LineBotApi, WebhookHandler
from get_random_text import get_random_text
from linebot.models import TextSendMessage, ImageSendMessage
import os
from dotenv import load_dotenv

access_token = os.getenv("CHANNEL_ACCESS_TOKEN")
secret = os.getenv("CHANNEL_SECRET")
line_bot_api = LineBotApi(access_token)   

load_dotenv()

def get_image(msg, token):
    try:
        if  msg == '椰咚' or msg == '禮志':
            # 如果有圖片網址，回傳圖片
            img_url = 'https://res.cloudinary.com/dbrf4i0rb/image/upload/v1717041883/Screenshot_2024-05-30_at_08.33.37_zi7k7l.png'
            img_message = ImageSendMessage(original_content_url=img_url, preview_image_url=img_url)
            line_bot_api.reply_message(token,img_message)
        elif msg == 'Lia' or msg == '粒鴨':
            img_url = 'https://res.cloudinary.com/dbrf4i0rb/image/upload/v1717052001/lia_hnwmmg.jpg'
            img_message = ImageSendMessage(original_content_url=img_url, preview_image_url=img_url)
            line_bot_api.reply_message(token,img_message)
        elif msg == '留真' or msg == '溜溜':
            img_url = 'https://res.cloudinary.com/dbrf4i0rb/image/upload/v1717050660/phbvy5pm0dxk2kcedhzy.jpg'
            img_message = ImageSendMessage(original_content_url=img_url, preview_image_url=img_url)
            line_bot_api.reply_message(token,img_message)
        elif msg == '彩領' or msg == '教授':
            img_url = 'https://res.cloudinary.com/dbrf4i0rb/image/upload/v1717051713/S__17547595_wwue5m.jpg'
            img_message = ImageSendMessage(original_content_url=img_url, preview_image_url=img_url)
            line_bot_api.reply_message(token,img_message)
        elif msg == '有娜' or msg == '芭比':
            img_url = 'https://res.cloudinary.com/dbrf4i0rb/image/upload/v1717051713/yuna_csimji.jpg'
            img_message = ImageSendMessage(original_content_url=img_url, preview_image_url=img_url)
            line_bot_api.reply_message(token,img_message)
        elif msg == '請鼓勵我':
            img_url = 'https://res.cloudinary.com/dbrf4i0rb/image/upload/v1717049784/artworks-wO5B7Svz2sILlOYm-n5A8fA-t500x500_zgrrpi.jpg'
            img_message = ImageSendMessage(original_content_url=img_url, preview_image_url=img_url)
            line_bot_api.reply_message(token,img_message)
        elif msg == 'itzy 想對我說...':
            result = get_random_text()
            text_message = TextSendMessage(text=result)
            line_bot_api.reply_message(token,text_message)
        else:
            # 如果 msg 不符合，回傳文字
            text_message = TextSendMessage(text='找不到相關圖片')
            line_bot_api.reply_message(token,text_message)
    except:
        print('error')
        return 'error'
    
    # 
        
