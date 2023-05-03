from telegram import Bot
import os

url = 'https://echobotrustambek.pythonanywhere.com/webhook'

TOKEN= os.environ['TOKEN']

bot = Bot(TOKEN)

print(bot.set_webhook(url))
print(bot.get_webhook_info())