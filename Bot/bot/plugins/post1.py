import random
from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from Bot.bot import Bot
from Bot.vars import Var

A = ["https://telegra.ph/file/944caf39b3988593b815f.jpg", "https://telegra.ph/file/c5aca1bc2f76c9cfd389a.jpg"]
h = random.choice(A)



@Bot.on_message(filters.command(["post"]))
async def post(bot, message):
    status_message = await message.reply_text("Making Post ...")
    hi = message.text.split(" ", maxsplit=1)[1]
    cmd = message.text.split(" ", maxsplit=1)[1]
    text= (
        "**🌀Hot Video XXX Video New Collection 🤤 🔥💧💦**\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n**📥𝗪𝗮𝘁𝗰𝗵 𝗢𝗻𝗹𝗶𝗻𝗲👀/ 𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱**\n\n👉{}\n👉{}\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n[✴️Install PlayerJet & Watch Unlimited Time💥](https://play.google.com/store/apps/details?id=com.rs.playerjet)\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬".format(
        cmd,hi
        )
    )
    
    await message.reply_photo(
    photo=h,
    caption=text, 
    parse_mode="Markdown"
    )
    await status_message.delete()
