import random
from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from Bot.bot import Bot
from Bot.vars import Var

@Bot.on_message(filters.command(["start", "help"]))
async def start(_, m: Message):
    await m.reply(
        f'**🔅Send Me Streaam Link Which You Want In Format.**'
    )


fuck = ["https://telegra.ph/file/e1803ea7e73c1d56f6105.jpg"]

@Bot.on_message()
async def post(bot, message):
    status_message = await message.reply_text("Making Post ...")
    hi = message.text
    cmd = message.text
    text= (
        "**Today  D€$! Premium video🥰🥰**\n\n**😍 WATCH ONLINE OR DOWNLOAD 📱**\n**(Just Install #PLAYERJET App from playstore)**\n**(💥 Fastest Speed No Buffering)**\n━━━━━━━━━━━━━━━━━\n**✅Download/Online Watch 720p👇**\n━━━━━━━━━━━━━━━━━\n👉{}\n👉{}\n━━━━━━━━━━━━━━━━━\n**Stay In Channel For More Videos 🔥**".format(
        cmd,hi
        )
    )
    
    await message.reply_photo(
    photo=random.choice(fuck),
    caption=text, 
    parse_mode="Markdown"
    )
    await status_message.delete()
