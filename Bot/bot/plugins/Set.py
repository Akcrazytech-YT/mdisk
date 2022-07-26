import logging
import requests
from random import random
import secrets
import time
from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from Bot.bot import Bot
from Bot.vars import Var
from urllib.parse import quote_plus
import traceback
import asyncio
import aiohttp
import string
import io
import os
import shutil
import sys

@Bot.on_message(filters.private & filters.text)
async def mdisk_convertor(client, message):
  if url_validator(message.text):
    id=message.text.split('/')[5]
    resp=requests.get(f'https://diskuploader.entertainvideo.com/v1/file/cdnurl?param={id}')
    response=resp.json()
    source=response ['source']
    name=response ['filename']
    msg=f"Mdisk Link Converted\nFile Name : {name}\n\n mpd : {source}"
    await message.reply_text(msg, parse_mode="markdown", disable_web_page_preview=True)
        
        
def url_validator(url):
  URLRegex = re.compile(
    r'^(?:http|ftp)s?://' # http:// or https://
    r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
    r'(?::\d+)?' # optional port
    r'(?:/?|[/?]\S+)$', re.IGNORECASE)
  return bool(re.match(URLRegex, url))
