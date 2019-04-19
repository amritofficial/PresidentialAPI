from flask import Flask, request

app = Flask(__name__)

@app.route('/data/all', methods=['GET'])
def get_data():
    if request.args.get('format') == None:
        return 'Route Works with JSON'

    return 'route works ' + request.args.get('format')

if __name__ == '__main__':
    app.run(debug=True)