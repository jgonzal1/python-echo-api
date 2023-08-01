from flask import Flask, request

app = Flask(__name__)

@app.route('/echo', methods=['POST', 'PUT', 'GET'])
def echo():
    response = {}
    if request.args:
        response["args"] = request.args
    if request.headers:
        response["headers"] = dict(request.headers)
    if request.data:
        response["data"] = request.data
    if request.is_json:
        response["json"] = request.json
    else:
        response["form"] = request.form
    return response

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
