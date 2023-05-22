from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, WorldXD!'

@app.route('/about')
def about():
    return 'About'