from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'I am Quzu bot that is created by Farid Jafarov for taking care for his quzu. I will be ready soon, I am under process right now. Love quzu <3'
