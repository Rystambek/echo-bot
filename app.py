from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api', methods= ['POST'])
def api():

    data = request.get_json(force=True)
    output = {'message':'Hello World'}
    return output

if __name__=='__main__':
    app.run(debug=True)