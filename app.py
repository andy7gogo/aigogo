import os
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)
# Channel Access Token
line_bot_api = LineBotApi('Pt4mHPX5fCHxN18Ag6wfT/wV2317PQa8Govm/QgfBZewnib1AA7fcSq9KhhF0Es7T4lDZ0EqjAQtKCNlHHPLAJf2Q5JcCxCcjWNvAgon7LgSM1uZdjrcg6sdegjCg14Mzl1cEv59H6+5CnTZ/a2q4AdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('b4d638b8e07773a8e2633d16cd8817b8')

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# 處理訊息 

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text.lower()

    if msg == 'hi':
        message = TemplateSendMessage(
        alt_text='Buttons template',
        template=ButtonsTemplate(
        thumbnail_image_url='https://i0.wp.com/www.womstation.com/wp-content/uploads/2018/11/%E9%9F%93%E5%9C%8B4.png?w=1280&ssl=1',
        title='第一個小功能',
        text='網頁測試',
        actions=[
            URITemplateAction(
                label='熱門youtube',
                uri='https://www.youtube.com/feed/trending'
            ),
            URITemplateAction(
                label='小新聞',
                uri='https://news.google.com/?hl=zh-TW&tab=wn1&gl=TW&ceid=TW:zh-Hant'
            ),
            MessageTemplateAction(
                label='天氣',
                text='https://www.google.com/search?source=hp&ei=0Nw7XuHSAaK2mAXexKKACg&q=%E5%A4%A9%E6%B0%A3&oq=%E5%A4%A9%E6%B0%A3&gs_l=psy-ab.12..0i70i256j0i131j0j0i131l7.457.3402..9212...1.0..1.57.466.10......0....1..gws-wiz.....0.4ONE6RnC3uU&ved=0ahUKEwjh-tTwzrznAhUiG6YKHV6iCKAQ4dUDCAw'
            )

                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)

    else:
    	message = TextSendMessage(text='請輸入hi')
    	line_bot_api.reply_message(event.reply_token, message)




if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)