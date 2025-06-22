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
SESSION = config("BQFqbogAi7-25RDHjKK8kGt7KNhTL6kkR15GCligoShrPorX4EnwwU-LVQ4nrEYSqjIEpxmK57hAcLoyFF44HcRv5Ws0bQeT2E1Yki6Y4PdvkYpOINisonLCjigLrWMWKCAulLjKvxxBp_6D_8TA-nky5nou4Z66QDAjVyUab3k-fyxbs223VagPW0L0VHVjRiGlhDNzcTrFHNlMtAqjqmy3n-Yb15VPFHhbNotSWBotYNDhRhtemjWJztIWWCfWSTb4POuj74SILXB1gAtShhNb9d5NqrBADLULbmKlQtpG9nkAB_jXBQxutDjMrNfeaFTeXqrVwXSkSqjjrI_LZjtg4h3mQQAAAAFdOGBhAA")
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
