from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.errors import UserNotParticipantError
import os
session = os.environ.get("SESSION")

class user():
    client = TelegramClient(session, 5367566, "641c80fcd5206311afd85bf78580ca4f")
    
user.client.run_untill_disconnect()
