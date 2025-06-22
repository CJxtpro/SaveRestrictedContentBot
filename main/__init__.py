#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("23752328")
API_HASH = config("d888eed9c6a5072bdfe09a6ece23171e")
BOT_TOKEN = config("7684998954:AAGJNP5E5jPXP2aHxbHKnnIEDv1OCRDz_ww")
SESSION = config("1BVtsOKEBuyY3l3xy10vDVD9OuN9AwWlaWdxNV-OtDitrnCfFUzBUYcDmaXDnTYQ1kzBtqyIOk4rOsMvxq7-MLBd8TarGMrtyhFtvi8z9-zor-kMQoLVM-5lADI5tGyhVYk4VQYPIbycWWLqjcW7X3o4PH-edg-AfgC1tLdPVbqzVqFjShspcX5-9w8gm6Yzc49h7DwEh3wnQv3gfi-IbHfZe39Bizti42K5QdKPWFy1WE6vZ2-otvWBRrLGqJBxxo9JF28XWkbXYyIIqiwzWIeCU5q-WH1V5kXJ8h6iZjOymbcPhJ8BzilGdH_feN-1Dgw6j53OfaaSSfh9X1xmaRq1ZG6GA554=")
FORCESUB = config("srcbotuse")
AUTH = config("5858943073")

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
