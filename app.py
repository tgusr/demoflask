from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Welcome to Harp tech Website! This is made using flask ^_^'
