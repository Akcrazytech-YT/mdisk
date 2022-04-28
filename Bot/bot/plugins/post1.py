import os
import time
import random
from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from Bot.bot import Bot
from Bot.vars import Var
from PIL import Image
from database.database import *
from database.db import *

thumb_image_path = Config.DOWNLOAD_LOCATION + "/" + str(Bot.from_user.id) + ".jpg"
if not os.path.exists(thumb_image_path):
            mes = await thumb(Bot.from_user.id)
            if mes != None:
                        m = await bot.get_messages(Bot.chat.id, mes.msg_id)
                        await m.download(file_name=thumb_image_path)
                        thumb_image_path = thumb_image_path

@Bot.on_message(filters.command(["start", "help"]))
async def start(_, m: Message):
    await m.reply(
        f'**🔅Send Me Streaam Link Which You Want In Format.**'
    )


@Bot.on_message()
async def post(bot, message):
            thumb_image_path = Config.DOWNLOAD_LOCATION + "/" + str(message.from_user.id) + ".jpg"
            status_message = await message.reply_text("Making Post ...")
            hi = message.text
            cmd = message.text
            text= (
                        "**Today  D€$! Premium video🥰🥰**\n\n**😍 WATCH ONLINE OR DOWNLOAD 📱**\n**(Just Install #PLAYERJET App from playstore)**\n**(💥 Fastest Speed No Buffering)**\n━━━━━━━━━━━━━━━━━\n**✅Download/Online Watch 720p👇**\n━━━━━━━━━━━━━━━━━\n👉{}\n👉{}\n━━━━━━━━━━━━━━━━━\n**Stay In Channel For More Videos 🔥**".format(
                                    cmd,hi
                        )
            )
            await message.reply_photo(
                        photo=thumb_image_path,
                        caption=text,
                        parse_mode="Markdown"
            )
            await status_message.delete()
