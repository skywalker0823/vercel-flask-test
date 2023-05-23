from flask import Flask, render_template as rt

app = Flask(__name__)
app.config['template_folder'] = 'templates'

@app.route('/')
def home():
    return rt('index.html')

@app.route('/about')
def about():
    return 'About'