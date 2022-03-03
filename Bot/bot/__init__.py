from ..vars import Var
from pyrogram import Client
from os import getcwd

Bot = Client(
    session_name="Bot",
    api_id=Var.API_ID,
    api_hash=Var.API_HASH,
    workdir="Bot",
    plugins={"root": "Bot/plugins"},
    bot_token=Var.BOT_TOKEN,
    sleep_threshold=Var.SLEEP_THRESHOLD,
    workers=Var.WORKERS,
)
