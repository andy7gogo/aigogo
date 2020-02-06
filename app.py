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
    msg = event.message.text

    if msg == '天氣':
        message = TemplateSendMessage(
        alt_text='Buttons template',
        template=ButtonsTemplate(
        thumbnail_image_url='https://s1.zerochan.net/Tsurumaki.Kokoro.600.2428613.jpg',
        title='早起',
        text='天氣',
        actions=[
            URITemplateAction(
                label='新竹',
                uri='https://www.google.com/search?ei=b70eXoaiL4fh-AaNlaKYAw&q=%E6%96%B0%E7%AB%B9%E5%A4%A9%E6%B0%A3&oq=%E6%96%B0%E7%AB%B9%E5%A4%A9%E6%B0%A3&gs_l=psy-ab.3..0i70i256j0i67j0i131j0i67l2j0l5.6189.7846..8034...0.1..1.73.658.14......0....1..gws-wiz.......0i71j0i131i67j0i131i67i70i256.YCtWlRDX34A&ved=0ahUKEwjGlcvwiIXnAhWHMN4KHY2KCDMQ4dUDCAs&uact=5'
            ),
            URITemplateAction(
                label='台北',
                uri='https://www.google.com/search?q=%E5%A4%A9%E6%B0%A3%E5%8F%B0%E5%8C%97%E5%85%AC%E9%A4%A8&oq=%E5%A4%A9%E6%B0%A3%E5%8F%B0%E5%8C%97%E5%85%AC%E9%A4%A8&aqs=chrome..69i57.5496j1j7&sourceid=chrome&ie=UTF-8'
            ),
            MessageTemplateAction(
                label='選單',
                text='back'
            )

                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)

    elif msg == '宅宅':
        message = TemplateSendMessage(
        alt_text='Buttons template',
        template=ButtonsTemplate(
        thumbnail_image_url='https://s1.zerochan.net/Tsurumaki.Kokoro.600.2390937.jpg',
        title='宅活',
        text='潛水',
        actions=[
            URITemplateAction(
                            label='巴哈姆特',
                            uri='https://www.gamer.com.tw/'
                        ),
            URITemplateAction(
                            label='梗',
                            uri='https://hornydragon.blogspot.com/'
                        ),
            MessageTemplateAction(
                label='選單',
                text='back'
            )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)


    elif msg == 'yt':
        message = TemplateSendMessage(
        alt_text='Buttons template',
        template=ButtonsTemplate(
        thumbnail_image_url='https://i.imgur.com/qtOnsvM.jpg',
        title='影片',
        text='潛水',
        actions=[
            URITemplateAction(
                            label='夯',
                            uri='https://www.youtube.com/feed/trending'
                        ),
            URITemplateAction(
                            label='nba',
                            uri='https://www.youtube.com/results?search_query=nba'
                        ),
            URITemplateAction(
                            label='onion',
                            uri='https://www.youtube.com/channel/UCzxN4G3s9uR9ao5_O5DoXmA/videos'
                        ),
            MessageTemplateAction(
                label='選單',
                text='back'
            )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)

    elif msg == 'x':
        message = TemplateSendMessage(
        alt_text='Buttons template',
        template=ButtonsTemplate(
        thumbnail_image_url='https://i.imgur.com/qtOnsvM.jpg',
        title='秘密影片',
        text='潛水',
        actions=[
            URITemplateAction(
                            label='nh',
                            uri='https://nhentai.net'
                        ),
            URITemplateAction(
                            label='po',
                            uri='https://pornhub.com'
                        ),
            MessageTemplateAction(
                label='選單',
                text='back'
            )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)



    else:
        message = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://s1.zerochan.net/Tsurumaki.Kokoro.600.2390937.jpg',
                    title='日常宅活',
                    text='懶人包',
                    actions=[
                        MessageTemplateAction(
                            label='點我',
                            text='宅宅'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/qtOnsvM.jpg',
                    title='youtube',
                    text='熱門',
                    actions=[
                        MessageTemplateAction(
                            label='點我',
                            text='yt'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://s1.zerochan.net/Tsurumaki.Kokoro.600.2428613.jpg',
                    title='早起',
                    text='天氣',
                    actions=[
                        MessageTemplateAction(
                            label='點我',
                            text='天氣'
                        )
                    ]
                )
            ]
        )
    )
        line_bot_api.reply_message(event.reply_token, message)

    
        

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)