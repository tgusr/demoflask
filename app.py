from flask import Flask, flash, redirect, render_template, request, url_for
import os, random
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/random')
def randi():
    r = random.randint(0, 9999)
    return str(r)

@app.route('/print/<SomeThing>')
def print_(SomeThing):
    return SomeThing

@app.route('/redirect')
def tg():
    return redirect('https://telegram.org')

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=os.environ.get("PORT"))
