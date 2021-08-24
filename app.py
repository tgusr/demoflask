from flask import Flask, flash, redirect, render_template, request, url_for
import os, random
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/random')
def randi():
    return random.randint("1", "100")

@app.route('/print/<SomeThing>')
def print_(SomeThing):
    return SomeThing

@app.route('/tg')
def tg():
    return redirect('https://t.me/anjana_ma')

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=os.environ.get("PORT"))
