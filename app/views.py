from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    if 1 == 1:
        return render_template('index.html')
    else:
        return "Foo"
