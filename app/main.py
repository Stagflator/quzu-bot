from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Quzu bot will be here soon.....'
