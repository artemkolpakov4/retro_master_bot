# bot.py

import os
import telegram

TOKEN = os.getenv("5931866701:AAH_LpY3o5KMrWJhckoVTlfP2IwIA5ESkFU")
CHAT_ID = os.getenv("-1001557949594")
bot = telegram.Bot(token=TOKEN)

async def send_message():
  message = 'Сообщение, которое нужно отправить'
  await bot.send_message(chat_id=CHAT_ID, text=message)

send_message()
