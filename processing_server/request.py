from flask import Flask, request, jsonify
from process_data import Process_Data
import requests

app = Flask(__name__)

url = 'http://127.0.0.1:5000/api/data'

@app.route('/')
@app.route('/data/all')
def process_request():

    query = request.args.get('format')

    if query == 'csv':
        return get_json_data()
    elif query == 'json' or query == None:
        return "Hello World"

def get_json_data():
    try:
        res = requests.get(url)
        return jsonify(res.json())
    except:
        return "Error!"

if __name__ == '__main__':
    app.run(port=5001, debug=True)
