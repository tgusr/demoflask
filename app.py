from flask import Flask
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.errors import UserNotParticipantError
app = Flask(__name__)
client = TelegramClient("1AZWarzYBuwjwd3Q7dSCE0dDEnFg7TX28tHaSCf0SmW442mpErfAyjl8MDXwU94k2FIKaHm_zu34Tt2ckJZ20bs6Co7Dv3PQKNKsWIz7rOlFR3t4fLlZPpPl4hVs81nFdDLt7jlOcJQAdM6Ju5ZlN294TRg7u1Uqn1-v1G0MRVVbkJ3z04qEGf7ycimW3-07-vYQue-QhoTxMwwjGuQjSkxHCTs6XrrEekhQiVy1lbypQl3OgTzrqVYwcG33cxmAb0ylI-iDYAqTRcYTQvZ576CIhqTCyKL5O5uBjBXXSIwuMPZ1E7hasu8MZyiBaJusNs_bucTMuCXMMdY0k_tevAMMzDbSmQSw=", 5367566, "641c80fcd5206311afd85bf78580ca4f")

@app.route('/')
def hello_world():
    return 'Hello, Welcome to Harp tech Website! This is made using flask ^_^'

@app.route('/fsub/<int:UsrID>')
def fsub_telethon(UsrID):
    try:
        await client(GetParticipantRequest("@Harp_Chat", UsrID))
        return "200"
    except:
        return "404"
