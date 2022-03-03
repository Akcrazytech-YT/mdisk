from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from Bot.bot import Bot
from Bot.vars import Var

@Bot.on_message(filters.command(["post"]))
async def post(bot, message):
    status_message = await message.reply_text("Making Post ...")
    hi = message.text.split(" ", maxsplit=1)[1]
    cmd = message.text.split(" ", maxsplit=1)[1]
    text= (
        "__Below Is Your Download Link__\n\n Link 🔗: {}\nLink: {}\n\n[Made By](https://pyrogram.org/)".format(
        cmd,hi
        )
    )
    
    await message.reply_photo(
    photo="https://telegra.ph/file/173093c36a565a8890e0a.jpg",
    caption=text, 
    parse_mode="Markdown"
    )
    await status_message.delete()
