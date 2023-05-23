from flask import Flask, render_template as rt

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, WorldXD!'

@app.route('/about')
def about():
    return 'About'