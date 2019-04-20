from flask import Flask, request, jsonify, Response, send_from_directory, send_file
import csv, datetime, re, json
from processing_server.process_data import Process_Data
import requests

app = Flask(__name__)

url = 'http://127.0.0.1:5000/api/data'

@app.route('/')
@app.route('/data/all')
def process_request():
    process_data = Process_Data()

    json_data = jsonify(get_json_data())
    query = request.args.get('format')

    # if the selected format is CSV return the customized CSV file as attachment
    if query == 'csv' or query is None:
       return process_data.create_json_csv(json_data)
    # if the selected format is JSON then return the customized JSON file
    elif query == 'json':
       return process_data.create_custom_json(json_data)

# call the API Endpoint to return a JSON response
def get_json_data():
    try:
        res = requests.get(url)
        return res.json()
    except:
        return "Error!"




