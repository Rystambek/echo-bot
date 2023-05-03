from telegram import Update
from telegram.ext import Updater, CallbackContext,CommandHandler


def start(update:Update,context:CallbackContext):
    update.message.reply_text('hello')