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


fuck = ["https://telegra.ph/file/443616c6fd4ac7cbbf05e.jpg","https://telegra.ph/file/f4ddb9e5f38c89254df59.jpg","https://telegra.ph/file/4c13bbd0e4100916d125c.jpg","https://telegra.ph/file/307d7839ca6246d05cf6f.jpg","https://telegra.ph/file/8312e9dda8e11019ca030.jpg","https://telegra.ph/file/23532c5f66f27f7592701.jpg","https://telegra.ph/file/60c1ba9debe262ba73730.jpg","https://telegra.ph/file/9c1bc9652df8596a7c3bd.jpg"]

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
