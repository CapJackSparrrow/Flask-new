from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/hello1")
def hello_world1():
    return "Hello, World!12"
@app.route("/hello2")
def hello_world2():
    return "Hello, World!34"

@app.route('/input_url')
def reuest_input():
    data = request.args.get('x')
    return 'this is my inout from url {}'.format(data)

@app.route('/test')
def test():
    a = 5+6
    return 'this is my func {}'.format(a)
if __name__=="__main__":
    app.run(host="0.0.0.0")