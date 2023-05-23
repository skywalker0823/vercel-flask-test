from flask import Flask, render_template as rt
from pathlib import Path

app = Flask(__name__, template_folder=Path(__file__).parent.parent / 'templates')

@app.route('/')
def home():
    return rt('index.html')

@app.route('/about')
def about():
    return 'About'