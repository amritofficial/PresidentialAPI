from flask import Flask, request

app = Flask(__name__)

@app.route('/')
@app.route('/data/all')
def process_data():
    return 'this is a Flask'

if __name__ == '__main__':
    app.run(debug=True)