from flask import Flask, jsonify
import json

app = Flask(__name__)

# load data from file and send it as a JSON response
@app.route('/api/data', methods=['GET'])
def get_data():
    file_name = 'data/data.json'
    file = open(file_name, 'r')
    json_data = json.load(file)

    return jsonify(json_data)

if __name__ == '__main__':
    app.run(debug=True)