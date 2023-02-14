from flask import Flask, request
import requests
import os 

app = Flask(__name__)

TOKEN = os.environ.get('TOKEN')

@app.route('/webhook', methods = ['POST'])
def webhook():
    data = request.get_json(force=True)
    
    chat_id = data['message']['from']['id']
    text = data['message']['text']

    payload = {
        "chat_id":chat_id,
        "text" : text
    }
    print(chat_id, text)
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    r = requests.get(url=url, params=payload )

    return 'ok'

