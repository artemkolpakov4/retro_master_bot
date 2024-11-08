# bot.py

import os
import telegram
import asyncio
import time
from aiocron import crontab
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

TOKEN = "5931866701:AAH_LpY3o5KMrWJhckoVTlfP2IwIA5ESkFU"
CHAT_ID = "-1001557949594"
bot = telegram.Bot(token=TOKEN)

async def send_message_weekly_update_2():
  message = 'Обновление Weekly Update v2'
  button = InlineKeyboardButton(text="YQL", url="https://yql.yandex-team.ru/Operations/672c8829d930343670edad06")
  keyboard = InlineKeyboardMarkup([[button]])
  await bot.send_message(chat_id=CHAT_ID, text=message, reply_markup=keyboard)

cron_job = crontab('* * * * *')(send_message_weekly_update_2)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        loop.run_forever()
    except:
        pass
