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
SESSION = config("BQFbu6AAvola7PfFCgE5UycdGT2FZr1t9LUARI2G-zaaOjrAFZRGRbhBs8RDU-tVgj7BN6nomrCM6mgRNEqedaMv07oCJjG6J8sgYOep6Av1gy0hjyz3EzdM_qBNn3dGBdavVHMO79EzAfqtwR6evMwZsyhzBx9bRItJriGfnTw9I42CIRXmcnU84USilsVe6vJXBb8WTYY21cDJAUs-QJdSYixWozovp36LB8cEB1yYvMXZ9zeUHFB_DNveqxQb5lg_erLkoD2ADdI1N0pYTB6nXms6MeUtctSlcDXgnnnVgCnxCoamdksukv7oxTB7LdKgy3zb5N1maqx3PAWlXcozrTVGiwAAAAFdOGBhAA")
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
