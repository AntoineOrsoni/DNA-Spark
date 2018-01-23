from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello, World!'


@app.route('/', methods=['POST'])
def helloPost():
    req = request.get_json()
    print(req)
    return 'Hello, POST'


app.run(host='127.0.0.1', port=5000)
