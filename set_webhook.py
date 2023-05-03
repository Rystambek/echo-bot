from telegram import Bot
import os

url = 'https://echobotrustambek.pythonanywhere.com/webhook'

TOKEN = '6162217632:AAGgQkGHbF2O3oaYbknbk9XhhVyMBAJjEdM'

bot = Bot(TOKEN)

print(bot.set_webhook(url))
print(bot.get_webhook_info())