from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,FlexSendMessage,PostbackEvent
)
from menu import Menu

import json



line_bot_api = LineBotApi('B5jc4AtNZG/I56Vt9l6KeS9zpZteoDMeHHDVYUu3MPM/uHWkeS/jADTA5oQLU9CLqGIeGqLQrXGusvOKpy/tTKBNgTVpl8giVd+r2NuNhMZeRkSp0gClfzvILB5xUcorlw8g5zYXX0KFkEa/fFr1EgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('1af6ae197eaf1b79b4ea466a29597aab')

reply = Menu()

    


def lambda_handler(event, context):
    print("============== Event START ================")
    print(event)
    print("============== Event END ================")
    @handler.add(MessageEvent, message=TextMessage)
    def handle_message(event):
        reply = Menu()
        if reply.is_Menu(event.message.text):
            print('111')
            line_bot_api.reply_message(
                event.reply_token,
                FlexSendMessage(alt_text='常見問題',contents=reply.get_menu_flex_message()))
    
    
        
        
        


    # get X-Line-Signature header value
    signature = event['headers']['x-line-signature']

    # get request body as text
    body = event['body']

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        return {
            'statusCode': 502,
            'body': json.dumps("Invalid signature. Please check your channel access token/channel secret.")
            }
    return {
        'statusCode': 200,
        'body': json.dumps("Hello from Lambda!")
        }