from telegram import Update
from telegram.ext import Updater, CallbackContext,CommandHandler
from handler import start
import os

TOKEN= '6162217632:AAEnncQeDNHOnSCAlMw0PTxbkJpAQQdL2X4'


updater = Updater(TOKEN)

dp =  updater.dispatcher

dp.add_handler(CommandHandler('start',start))

updater.start_polling()
updater.idle()
