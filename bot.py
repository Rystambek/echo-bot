from telegram import Update
from telegram.ext import Updater, CallbackContext,CommandHandler
from handler import start
import os

TOKEN= os.environ['TOKEN']


updater = Updater(TOKEN)

dp =  updater.dispatcher

dp.add_handler(CommandHandler('start',start))

updater.start_polling()
updater.idle()
