# bot.py

import asyncio
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, ContextTypes, JobQueue

TOKEN = "5931866701:AAH_LpY3o5KMrWJhckoVTlfP2IwIA5ESkFU"
CHAT_ID = "-1001557949594"

async def send_message_weekly_update_2(context: ContextTypes.DEFAULT_TYPE):
    message = 'Обновление Weekly Update v2'
    button = InlineKeyboardButton(
        text="YQL", 
        url="https://yql.yandex-team.ru/Operations/672c8829d930343670edad06"
    )
    keyboard = InlineKeyboardMarkup([[button]])
    await context.bot.send_message(
        chat_id=CHAT_ID, 
        text=message, 
        reply_markup=keyboard
    )

async def main():
    application = ApplicationBuilder().token(TOKEN).build()

    job_queue = application.job_queue
    job_queue.run_repeating(
        send_message_weekly_update_2, 
        interval=60, 
        first=0
    )

    await application.run_polling()

if __name__ == '__main__':
    asyncio.run(main())
