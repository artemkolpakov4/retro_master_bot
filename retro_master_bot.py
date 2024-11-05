# bot.py

import os
import telegram
import asyncio
import time

TOKEN = "5931866701:AAH_LpY3o5KMrWJhckoVTlfP2IwIA5ESkFU"
CHAT_ID = "-1001557949594"
bot = telegram.Bot(token=TOKEN)

async def send_message():
  message = 'Сообщение, которое нужно отправить'
  await bot.send_message(chat_id=CHAT_ID, text=message)

async def main():
    while True:
        await send_message()
        await asyncio.sleep(5)

asyncio.run(main())
