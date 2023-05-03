from telegram import Update
from telegram.ext import Updater, CallbackContext,CommandHandler
import os

TOKEN= os.environ['TOKEN']

def start(update:Update,context:CallbackContext):
    update.message.reply_text('hello')

updater = Updater(TOKEN)

dp =  updater.dispatcher

dp.add_handler(CommandHandler('start',start))

updater.start_polling()
updater.idle()
