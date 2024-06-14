import re
import os
from os import environ
from pyrogram import enums
from Script import script
from dotenv import load_dotenv

import asyncio
import json
from collections import defaultdict
from typing import Dict, List, Union
from pyrogram import Client

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

class evamaria(Client):
    filterstore: Dict[str, Dict[str, str]] = defaultdict(dict)
    warndatastore: Dict[
        str, Dict[str, Union[str, int, List[str]]]
    ] = defaultdict(dict)
    warnsettingsstore: Dict[str, str] = defaultdict(dict)

    def __init__(self):
        name = self.__class__.__name__.lower()
        super().__init__(
            ":memory:",
            plugins=dict(root=f"{name}/plugins"),
            workdir=TMP_DOWNLOAD_DIRECTORY,
            api_id=APP_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            parse_mode=enums.ParseMode.HTML,
            sleep_threshold=60
        )

SESSION = os.environ.get('SESSION', 'Media_search')
API_ID = int(os.environ.get('API_ID', '3261311'))
API_HASH = os.environ.get('API_HASH', '41377ec3060b15a5105dbe1e8af95c99')
BOT_TOKEN = os.environ.get('BOT_TOKEN', '7284021150:AAEHsJ2WLs7lCvXlN4mRbEsrcRsS6Wh1_Uc')

# Bot settings
CACHE_TIME = int(os.environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(os.environ.get('USE_CAPTION_FILTER', False))
PICS = os.environ.get('PICS', 'https://telegra.ph/file/2992a480cae2bc0de1c39.jpg https://telegra.ph/file/76e7b5e94430b84a3d2b2.jpg https://telegra.ph/file/3544a8773740b0412c9dd.jpg https://telegra.ph/file/4b1c7004ea8bd3fed8df9.jpg https://telegra.ph/file/a02e47d932adc336740fa.jpg').split()
NOR_IMG = os.environ.get('NOR_IMG', "https://telegra.ph/file/3ae93b58201a8d5f42f64.jpg")
SPELL_IMG = os.environ.get('SPELL_IMG', "https://telegra.ph/file/b58f576fed14cd645d2cf.jpg")

# Welcome area
MELCOW_IMG = os.environ.get('MELCOW_IMG', "https://telegra.ph/file/e54cae941b9b81f13eb71.jpg")
MELCOW_VID = os.environ.get('MELCOW_VID', "")

# Admins, Channels & Users
id_pattern = re.compile(r'^.\d+$')
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMINS', '1869495895').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in os.environ.get('CHANNELS', '-1001481355049 -1001695699917').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in os.environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_grp = os.environ.get('AUTH_GROUP')
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None
support_chat_id = os.environ.get('SUPPORT_CHAT_ID')

# This is required for the plugins involving the file system.
TMP_DOWNLOAD_DIRECTORY = os.environ.get("TMP_DOWNLOAD_DIRECTORY", "./DOWNLOADS/")

# Command
COMMAND_HAND_LER = os.environ.get("COMMAND_HAND_LER", "/")

# MongoDB information
DATABASE_URI = os.environ.get('DATABASE_URI', 'mongodb+srv://amal:amal@cluster0.xs86qqm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
DATABASE_NAME = os.environ.get('DATABASE_NAME', 'req')
COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Telegram_files')
MONGO_URL = os.environ.get('MONGO_URL', "")

#Downloader
DOWNLOAD_LOCATION = environ.get("DOWNLOAD_LOCATION", "./DOWNLOADS/AudioBoT/")

# FSUB

auth_channel = environ.get('AUTH_CHANNEL', '-1001839733576')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else False
AUTH_CHANNEL2 = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else False
# Set to False inside the bracket if you don't want to use Request Channel else set it to Channel ID
REQ_CHANNEL = environ.get("REQ_CHANNEL", 'False')
REQ_CHANNEL = int(REQ_CHANNEL) if REQ_CHANNEL and id_pattern.search(REQ_CHANNEL) else False
JOIN_REQS_DB = environ.get("JOIN_REQS_DB", DATABASE_URI)

#url links
SHORTLINK_URL = environ.get('SHORTLINK_URL', '')
SHORTLINK_API = environ.get('SHORTLINK_API', '')
IS_SHORTLINK = bool(environ.get('IS_SHORTLINK', False))

#Openai
AI = is_enabled((environ.get("AI","False")), False)
OPENAI_API = environ.get("OPENAI_API"," ")
AI_LOGS = int(environ.get("AI_LOGS", "-1002049486679")) #GIVE YOUR NEW LOG CHANNEL ID TO STORE MESSAGES THAT THEY SEARCH IN BOT PM.... [ i have added this to keep an eye on the users message, to avoid misuse of Bot ]


#Auto approve
CHAT_ID = [int(app_chat_id) if id_pattern.search(app_chat_id) else app_chat_id for app_chat_id in environ.get('CHAT_ID', '0').split()]
TEXT = environ.get("APPROVED_WELCOME_TEXT", "Hello {mention} Welcome To {title}\n\n🔰 ᴡᴇ ᴘʀᴏᴠɪᴅᴇ ᴍᴀʟᴀʏᴀʟᴀᴍ, ᴛᴀᴍɪʟ, ʜɪɴᴅɪ, ᴋᴀɴɴᴀᴅᴀ, ᴛᴇʟᴜɢᴜ, ᴀɴᴅ ᴇɴɢʟɪꜱʜ ᴍᴏᴠɪᴇꜱ, ɪɴᴄʟᴜᴅɪɴɢ ɴᴇᴡʟʏ ʀᴇʟᴇᴀꜱᴇᴅ ᴍᴏᴠɪᴇꜱ.")
APPROVED = environ.get("APPROVED_WELCOME", "on").lower()
WELCOME_TEXT = environ.get("APPROVED_WELCOME_TEXT", "Hello {mention} Welcome To {title}\n\n🔰 ᴡᴇ ᴘʀᴏᴠɪᴅᴇ ᴍᴀʟᴀʏᴀʟᴀᴍ, ᴛᴀᴍɪʟ, ʜɪɴᴅɪ, ᴋᴀɴɴᴀᴅᴀ, ᴛᴇʟᴜɢᴜ, ᴀɴᴅ ᴇɴɢʟɪꜱʜ ᴍᴏᴠɪᴇꜱ, ɪɴᴄʟᴜᴅɪɴɢ ɴᴇᴡʟʏ ʀᴇʟᴇᴀꜱᴇᴅ ᴍᴏᴠɪᴇꜱ.")
JOIN_CHANNEL_TEXT = environ.get("JOIN_CHANNEL_TEXT", "𝙲𝚒𝚗𝚎𝙵𝚕𝚒𝚡 🎪 Mᴏᴠɪᴇsx")
JOIN_CHANNEL_LINK = environ.get("JOIN_CHANNEL_LINK", "https://t.me/CineflixXLinks")

# Others
SUPPORT_CHAT_ID = int(support_chat_id) if support_chat_id and id_pattern.search(support_chat_id) else None
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '0').split()]
PORT = os.environ.get("PORT", "8080")
MAX_BTN = int(environ.get('MAX_BTN', "7"))
S_GROUP = environ.get('S_GROUP',"https://t.me/CineflixXLinks")
MAIN_CHANNEL = environ.get('MAIN_CHANNEL',"https://t.me/CineflixXLinks")
#Must change this link to work redirect (FILE_FORWORD)
FILE_FORWARD = environ.get('FILE_FORWARD',"https://t.me/CineflixXLinks")
MSG_ALRT = environ.get('MSG_ALRT', '𝑪𝑯𝑬𝑪𝑲 & 𝑻𝑹𝒀 𝑨𝑳𝑳 𝑴𝒀 𝑭𝑬𝑨𝑻𝑼𝑹𝑬𝑺')
FILE_CHANNEL = int(environ.get('FILE_CHANNEL', 0))
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002049486679'))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'CineflixXLinks')
AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "True")), True)
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "True")), True)
IMDB = is_enabled((environ.get('IMDB', "False")), False)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CUSTOM_FILE_CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", f"{script.IMDB_TEMPLATE_TXT}")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"
