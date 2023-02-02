from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler
from bot_commands import *
import emoji




app = ApplicationBuilder().token("token").build()

app.add_handler(CommandHandler('hello', hello_command))
app.add_handler(CommandHandler('time', time_command))
app.add_handler(CommandHandler('help', help_command))
app.add_handler(CommandHandler('sum', sum_command))
app.add_handler(CommandHandler('untiltheny', untiltheny_command))
print(emoji.emojize(f':thumbs_up:'))


print('Server start')
app.run_polling()
