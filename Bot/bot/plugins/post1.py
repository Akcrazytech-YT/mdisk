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


fuck = ["https://telegra.ph/file/f4ddb9e5f38c89254df59.jpg","https://telegra.ph/file/f4ddb9e5f38c89254df59.jpg"]



@Bot.on_message()
async def post(bot, message):
    status_message = await message.reply_text("Making Post ...")
    hi = message.text
    cmd = message.text
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
