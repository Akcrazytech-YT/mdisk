import os
import time
import random
from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from Bot.bot import Bot
from Bot.vars import Var
from pyrogram.enums.parse_mode import ParseMode

fuk="https://te.legra.ph/file/721510ad14d25ac18004d.jpg"

@Bot.on_message(filters.command(["start", "help"]))
async def start(_, m: Message):
    await m.reply(
        f'**🔅Send Me Streaam Link Which You Want In Format.**'
    )


@Bot.on_message()
async def post(bot, message):
    valid_url=[]
    text=message.text.split()
    reply_text="💥TODAY BEST NEW VIDEOS 👇\n\n"
    for url in text:
        if url_validator(url):
            valid_url.append(url)
    for x in range(len(valid_url)):
        reply_text=reply_text + f"VIDEO {str(x+1)})\n{valid_url[x]}\n\n"
    reply_text=reply_text+"━━━━━━━━━━━━━━━\n\nHow To Watch Tutorial 👇\n\nhttps://t.me/open_streaam/14"
    await message.reply_text(reply_text, parse_mode="markdown", disable_web_page_preview=True)        

# https://github.com/django/django/blob/stable/1.3.x/django/core/validators.py#L45

def url_validator(url):
    URLRegex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return bool(re.match(URLRegex, url))
