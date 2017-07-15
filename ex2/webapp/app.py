import os
from flask import Flask, render_template, request
from sklearn.naive_bayes import MultinomialNB
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ''
    if request.method == "POST":
        text = request.form['text']
        p = clf.predict([[text.count('H'), text.count('Y'), text.count('S')]])
        result = p[0]
    return render_template('index.html', result = result)

if __name__ == '__main__':
    df = pd.read_excel('NB.xlsx', sheetname=1)
    X = df.ix[:, 1:4]
    Y = df.分類
    clf = MultinomialNB()
    clf.fit(X, Y)

    app.run()
