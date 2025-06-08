# DON'T add anything here just add in render's secret or env section 
from os import environ

API_ID = int(environ.get("API_ID", "24731191"))
API_HASH = environ.get("API_HASH", "ca156f58ad03bb5e350c855bb82e9991")
BOT_TOKEN = environ.get("BOT_TOKEN", "")
