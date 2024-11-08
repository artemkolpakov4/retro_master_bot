import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import asyncio

# Вставьте сюда ваш токен
TOKEN = "5931866701:AAH_LpY3o5KMrWJhckoVTlfP2IwIA5ESkFU"
CHAT_ID = "-1001557949594"

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)
    
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
    scheduler = AsyncIOScheduler()
    scheduler.add_job(send_message_weekly_update_2, "interval", seconds=10, args=[application])
    scheduler.start()
    await application.run_polling()

if __name__ == '__main__':
    await main()
