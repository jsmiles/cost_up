from flask import Flask, request, jsonify
from processing import data_parser

app = Flask(__name__)


@app.route('/', methods=['POST'])
def my_api():

    data = request.get_json()
    return_data = data_parser(data)
    return jsonify(return_data)


if __name__ == '__main__':
    app.run(debug=True)
