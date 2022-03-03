from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from Bot.bot import Bot
from Bot.vars import Var

@Bot.on_message(filters.command(["post"]))
async def post(bot, message):
    status_message = await message.reply_text("Making Post ...")
    sex = message.text.split(" ", maxsplit=1)[1]
    cmd = message.text.split(" ", maxsplit=1)[1]
    text= (
        "<b>🌀Hot Video XXX Video New Collection 🤤 🔥💧💦</b>\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n📥𝗪𝗮𝘁𝗰𝗵 𝗢𝗻𝗹𝗶𝗻𝗲👀 and 𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱\n\n👉<b>{}</b>\n👉<b>{}</b>\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n".format(
            cmd,sex
        )
    )
    
     await message.reply_photo(
          photo="https://telegra.ph/file/173093c36a565a8890e0a.jpg",
          caption=text,
          disable_notification=True,
          reply_to_message_id=reply_to_id,
        )
        await status_message.delete()
