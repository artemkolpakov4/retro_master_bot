# bot.py

import os
import telegram
import asyncio
import time
from aiocron import crontab

TOKEN = "5931866701:AAH_LpY3o5KMrWJhckoVTlfP2IwIA5ESkFU"
CHAT_ID = "-1001557949594"
bot = telegram.Bot(token=TOKEN)

async def send_message():
  message = 'Сообщение, которое нужно отправить'
  await bot.send_message(chat_id=CHAT_ID, text=message)

@crontab('0 12 * * 2,4')
async def scheduled_send_message():
    await send_message()

async def main():
    while True:
        await asyncio.sleep(1)

if __name__ == '__main__':
  asyncio.run(main())
