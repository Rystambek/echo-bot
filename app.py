from telegram.ext import Updater, CommandHandler,CallbackQueryHandler,Dispatcher
from telegram import Update,Bot
from handler import start
from flask import Flask, request
import os

# get token from environment variable
TOKEN = '6162217632:AAGgQkGHbF2O3oaYbknbk9XhhVyMBAJjEdM'

bot = Bot(token=TOKEN)

app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    return 'OK'

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/webhook', methods=["POST", "GET"])
def hello():
    if request.method == 'GET':
        return 'flask is working'
    elif request.method == "POST":
        data = request.get_json(force = True)
        
        dp: Dispatcher = Dispatcher(bot, update_queue=None, workers=0)
        update:Update = Update.de_json(data, bot)
    
        #update 
                
        dp.add_handler(CommandHandler("start",start))

        dp.process_update(update)
        return 'ok'