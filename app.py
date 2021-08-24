from flask import Flask, flash, redirect, render_template, request, url_for
import os
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/print/<SomeThing>')
def print_(SomeThing):
    return SomeThing

@app.route('/tg')
def tg():
    return redirect(url_for('https://t.me/anjana_ma'))

if __name__ == '__main__':
   app.run(port=os.environ.get("PORT"))
