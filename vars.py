# DON'T add anything here just add in render's secret or env section 
from os import environ

API_ID = int(environ.get("API_ID", "26231033"))
API_HASH = environ.get("API_HASH", "23905191485be2fb424e89d503e9d80c")
BOT_TOKEN = environ.get("BOT_TOKEN", "")
