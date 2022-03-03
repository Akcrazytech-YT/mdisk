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
        "**Below Is Your Download Link\n\n Link 🔗: {}\nLink: {} ".format(
        cmd,hi
        )
    )
    
    await message.reply_photo(
    photo="https://telegra.ph/file/173093c36a565a8890e0a.jpg",
    caption=text
    )
    await status_message.delete()
