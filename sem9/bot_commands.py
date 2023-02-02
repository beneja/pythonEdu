from telegram import Update
from telegram.ext import Updater, CommandHandler, ContextTypes, MessageHandler
import datetime


async def hello_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text((f'Привет {update.effective_user.first_name}. Пора учиться программировать'))

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
     await update.message.reply_text(f'/hi\n/time\n/help')

async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'{datetime.datetime.now().time()}')

async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} + {y} = {x+y}')

async def untiltheny_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    now = datetime.datetime.today()
    NY = datetime.datetime(2024, 1, 1)
    d = NY-now                  
    mm, ss = divmod(d.seconds, 60)
    hh, mm = divmod(mm, 60)
    await update.message.reply_text(f'До Нового года {d.days} дней, {hh} часов, {mm} минут, {ss} секунд')