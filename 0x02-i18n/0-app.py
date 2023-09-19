#!/usr/bin/env python3
"""a script that starts a flask application"""
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET'], stri)
def hello():
    ''' returns a simple page'''
    return render_template('0-index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
