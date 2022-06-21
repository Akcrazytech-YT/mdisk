import os
import time
import random
from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from Bot.bot import Bot
from Bot.vars import Var

fuk="https://te.legra.ph/file/721510ad14d25ac18004d.jpg"

@Bot.on_message(filters.command(["start", "help"]))
async def start(_, m: Message):
    await m.reply(
        f'**🔅Send Me Streaam Link Which You Want In Format.**'
    )


@Bot.on_message()
async def post(bot, message):
            status_message = await message.reply_text("Making Post ...")
            hi = message.text
            cmd = message.text
            text= (
                        "**📥 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝 𝐋𝐢𝐧𝐤𝐬/👀𝐖𝐚𝐭𝐜𝐡 𝐎𝐧𝐥𝐢𝐧𝐞👇**\n\n**(Just Install #PLAYERJET App from playstore)**\n**(💥 Fastest Speed No Buffering)**\n━━━━━━━━━━━━━━━━━\n**Video 1.👉 {}**\n**Video 1.👉 {}**\n━━━━━━━━━━━━━━━━━\n**How To Watch Tutorial 👇**\n**https://t.me/open_streaam/14**".format(
                                    cmd,hi
                        )
            )
            await message.reply_photo(
                        photo=fuk,
                        caption=text,
                        parse_mode="Markdown"
            )
            await status_message.delete()
