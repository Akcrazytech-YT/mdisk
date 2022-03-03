import random
from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from Bot.bot import Bot
from Bot.vars import Var

fuck = ["https://telegra.ph/file/944caf39b3988593b815f.jpg", "https://telegra.ph/file/c5aca1bc2f76c9cfd389a.jpg","https://telegra.ph/file/ceafda01bfce443939c51.jpg","https://telegra.ph/file/173093c36a565a8890e0a.jpg","https://telegra.ph/file/22ec5ab752cc953ef7acb.jpg","https://telegra.ph/file/85446d617badc3ab0dc1c.jpg","https://telegra.ph/file/32e3e6f58286fe699d37b.jpg"]



@Bot.on_message()
async def post(bot, message):
    status_message = await message.reply_text("Making Post ...")
    hi = message.text.split("", maxsplit=0)[0]
    cmd = message.text.split("", maxsplit=0)[0]
    text= (
        "**🌀Hot Video XXX Video New Collection 🤤 🔥💧💦**\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n**📥𝗪𝗮𝘁𝗰𝗵 𝗢𝗻𝗹𝗶𝗻𝗲👀/ 𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱**\n\n👉{}\n👉{}\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n[✴️Install PlayerJet & Watch Unlimited Time💥](https://play.google.com/store/apps/details?id=com.rs.playerjet)\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬".format(
        cmd,hi
        )
    )
    
    await message.reply_photo(
    photo=random.choice(fuck),
    caption=text, 
    parse_mode="Markdown"
    )
    await status_message.delete()
