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
    except:
        print(body)             # 如果發生錯誤，印出收到的內容
    return 'OK'                 # 驗證 Webhook 使用，不能省略
if __name__ == "__main__":
    app.run()

















