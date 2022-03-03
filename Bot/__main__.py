import os
import sys
import glob
import asyncio
import logging
import importlib
from pathlib import Path
from pyrogram import idle
from .bot import Bot
from .vars import Var

ppath = "Bot/bot/plugins/*.py"
files = glob.glob(ppath)

loop = asyncio.get_event_loop()

async def start_services():
    print('\n')
    print('------------------- Initalizing Telegram Posts Bot -------------------')
    await Bot.start()
    print('\n')
    print('---------------------- DONE ----------------------')
    print('\n')
    print('------------------- Importing -------------------')
    for name in files:
        with open(name) as a:
            patt = Path(a.name)
            plugin_name = patt.stem.replace(".py", "")
            plugins_dir = Path(f"Bot/bot/plugins/{plugin_name}.py")
            import_path = ".plugins.{}".format(plugin_name)
            spec = importlib.util.spec_from_file_location(import_path, plugins_dir)
            load = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(load)
            sys.modules["Bot.bot.plugins." + plugin_name] = load
            print("Imported => " + plugin_name)
    print('\n')
    print('----------------------- Started Bot -----------------------')
    print('                        bot =>> {}'.format((await Bot.get_me()).first_name))
    await idle()

if __name__ == '__main__':
    try:
        loop.run_until_complete(start_services())
    except KeyboardInterrupt:
        print('----------------------- Service Stopped -----------------------')
