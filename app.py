from flask import Flask
import youtube_dl
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Welcome to Harp tech Website! This is made using flask ^_^'

@app.route('/print/<SomeThing>')
def print_(SomeThing):
    return SomeThing
