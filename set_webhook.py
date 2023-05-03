# from telegram import Bot
# import os

# url = 'https://echobotrustambek.pythonanywhere.com/webhook'

# TOKEN = '6162217632:AAEnncQeDNHOnSCAlMw0PTxbkJpAQQdL2X4'

# bot = Bot(TOKEN)

# print(bot.set_webhook(url))
# print(bot.get_webhook_info())
import requests
import os

url = 'https://echobotrustambek.pythonanywhere.com/webhook'

Token = '6004154698:AAEo2pZT8WqoCqRGAXZchoYMtdgozcq3Kbc'

payload = {
    "url":url
}

r = requests.get(f"https://api.telegram.org/bot{Token}/setWebhook", params=payload)
r = requests.get(f"https://api.telegram.org/bot{Token}/GetWebhookInfo", params=payload)



print(r.json())