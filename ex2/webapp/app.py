import os
from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    result = ''
    if request.method == "POST":
        text = request.form['text']
        result = 'ひどい'
    return render_template('index.html', result = result)

if __name__ == '__main__':
    app.run()
