from flask import Flask, request, jsonify
import telegram
import os 

TOKEN = os.environ.get('TOKEN')
bot = telegram.Bot(Token=TOKEN)

app = Flask(__name__)
def home():
    html = '''
    <h1> This is a home page </h1>
    <p> This is a paragraph </p>
    '''
    print(TOKEN)
    return html

@app.route('/api', methods= ['POST'])
def api():

    data = request.get_json(force=True)
    chat_id = 996172963
    bot.sendMesage(chat_id = chat_id, text= 'Salom')
    return jsonify(data)

if __name__=='__main__':
    app.run(debug=True)