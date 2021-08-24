from flask import Flask
from c import c
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Welcome to Harp tech Website! This is made using flask ^_^'

@app.route('/fsub/<int:UsrID>')
async def fsub_telethon(UsrID):
    try:
        with c as client:
            await c(GetParticipantRequest("@Harp_Chat", UsrID))
        return "200"
    except:
        return "404"
