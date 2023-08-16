import asyncio
import logging
import os
import sys
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import RPCError
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", 0))
PORT = int(os.environ.get("PORT", 8080))
layer = int(os.environ.get("LAYER", 1))
class Bot(Client):
    def __init__(self):
        super().__init__(
            "MyBot",
            api_id=int(os.environ.get("API_ID", 0)),
            api_hash=os.environ.get("API_HASH", ""),
            bot_token=os.environ.get("BOT_TOKEN", ""),
            plugins=dict(root="plugins"),
            sleep_threshold=5,
        )
    async def start(self):
        b_users, b_chats = await db.get_banned()
        temp.BANNED_USERS = b_users
        temp.BANNED_CHATS = b_chats
        await super().start()
        await Media.ensure_indexes()
        me = await self.get_me()
        temp.ME = me.id
        temp.U_NAME = me.username
        temp.B_NAME = me.first_name
        self.username = '@' + me.username
        logging.getLogger("pyrogram").setLevel(logging.ERROR)
        logging.info(f"{me.first_name} with for Pyrogram v{__version__} (Layer {layer}) started on {me.username}.")
        logging.info(LOG_STR)
        logging.info(script.LOGO)
        tz = pytz.timezone('Asia/Kolkata')
        today = date.today()
        now = datetime.now(tz)
        time = now.strftime("%H:%M:%S %p")
        await self.send_message(chat_id=LOG_CHANNEL, text=script.RESTART_TXT.format(today, time))
        app = web.AppRunner(await web_server())
        await app.setup()
        bind_
