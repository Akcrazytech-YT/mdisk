import os

class Config(object):
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
  APP_ID = int(os.environ.get("APP_ID", 12345))
  API_HASH = os.environ.get("API_HASH")
  DOWNLOAD_LOCATION = "./DOWNLOADS"
  DB_URI = os.environ.get("DATABASE_URL", "")
