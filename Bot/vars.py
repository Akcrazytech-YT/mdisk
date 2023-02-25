from os import environ
from dotenv import load_dotenv

load_dotenv()


class Var(object):
    API_ID = int(environ.get("API_ID"))
    API_HASH = str(environ.get("API_HASH"))
    BOT_TOKEN = str(environ.get("BOT_TOKEN"))
    ADMIN = [2018327763]
