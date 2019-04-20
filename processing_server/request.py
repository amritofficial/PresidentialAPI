from flask import Flask, request
from processing_server.process_data import Process_Data
import requests

app = Flask(__name__)

url = 'http://127.0.0.1:5000/api/data'

@app.route('/')
@app.route('/data/all')
def process_request():
    process_data = Process_Data()
    query = request.args.get('format')

    print(query)

    return 'this is a Flask'

if __name__ == '__main__':
    app.run(port=5001, debug=True)