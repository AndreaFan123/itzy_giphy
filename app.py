from flask import Flask, request

# 載入 LINE Message API 相關函式庫
from linebot import LineBotApi, WebhookHandler
from dotenv import load_dotenv
from get_img import get_image
import json
import os


load_dotenv()

app = Flask(__name__)


@app.route("/callback", methods=['POST'])
def callback():
    body = request.get_data(as_text=True)                    # 取得收到的訊息內容
    try:
        json_data = json.loads(body)                         # json 格式化訊息內容
        secret = os.getenv("CHANNEL_SECRET")
        handler = WebhookHandler(secret)                     # 確認 secret 是否正確
        signature = request.headers['X-Line-Signature']      # 加入回傳的 headers
        handler.handle(body, signature)                      # 綁定訊息回傳的相關資訊
        tk = json_data['events'][0]['replyToken']            # 取得回傳訊息的 Token
        msg = json_data['events'][0]['message']['text']
        get_image(msg, tk)
        
        # if  msg == '椰咚' or msg == '禮志':
        #     # 如果有圖片網址，回傳圖片
        #     img_url = 'https://res.cloudinary.com/dbrf4i0rb/image/upload/v1717041883/Screenshot_2024-05-30_at_08.33.37_zi7k7l.png'
        #     img_message = ImageSendMessage(original_content_url=img_url, preview_image_url=img_url)
        #     line_bot_api.reply_message(tk,img_message)
        # elif msg == '請鼓勵我':
        #     img_url = 'https://res.cloudinary.com/dbrf4i0rb/image/upload/v1717049784/artworks-wO5B7Svz2sILlOYm-n5A8fA-t500x500_zgrrpi.jpg'
        #     img_message = ImageSendMessage(original_content_url=img_url, preview_image_url=img_url)
        #     line_bot_api.reply_message(tk,img_message)
        # else:
        #     # 如果 msg 不符合，回傳文字
        #     text_message = TextSendMessage(text='找不到相關圖片')
        #     line_bot_api.reply_message(tk,text_message)
    except:
        print(body)             # 如果發生錯誤，印出收到的內容
    return 'OK'                 # 驗證 Webhook 使用，不能省略
if __name__ == "__main__":
    app.run()

















