from flask import Flask, request

app = Flask(__name__)


@app.route('/echo', methods=['POST', 'PUT'])
def echo():
    if request.is_json:
        return request.json
    else:
        return request.form

