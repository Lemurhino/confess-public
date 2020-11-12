import configparser
import logging
import codecs

from json import loads

log = logging.getLogger(__name__)

CONFIG_FILE = "./data/config.ini"

config = configparser.ConfigParser()
config.read_file(codecs.open(CONFIG_FILE, "r", "utf-8"))

# bot-info.
BOT_TOKEN = config.get("Bot", "bot_token", fallback=None)
if not BOT_TOKEN:
    raise Exception("'bot_token' is missing!")

BOT_PREFIX = config.get("Bot", "bot_prefix", fallback="!").strip(" ")
SPECIAL_USERS_IDS = [int(id_) for id_ in loads(config.get("Bot", "special_user_ids", fallback="[]"))]
CHANNEL_ID = config.get("Bot", "channel_id").strip(" ")
if not CHANNEL_ID:
    raise Exception("'channel_id is missing!")
GUILD_ID = config.get("Bot", "guild_id").strip(" ")
if not GUILD_ID:
    raise Exception("'guild_id' is missing!")
LOG_ID = config.get("Bot", "log_channel_id").strip(" ")
if not LOG_ID:
    raise Exception("'log_id' is missing!")
log.info(f"Special users: {', '.join([str(a) for a in SPECIAL_USERS_IDS])}")
# Configure per server.
"""
GUILD_ID: int = config.getint("TriggerConfig", "guild_id")
VERIFICATION_TRIGGER_CHANNEL_ID: int = config.getint("TriggerConfig", "verification_trigger_channel_id")
VERIFICATION_TRIGGER_MESSAGE_ID: int = config.getint("TriggerConfig", "verification_trigger_message_id")
VERIFICATION_TRIGGER_EMOJI: str = config.get("TriggerConfig", "verification_trigger_emoji")

VERIFICATION_CHANNEL_CATEGORY_ID: int = config.getint("AuthConfig", "verification_channel_category_id")
VERIFICATION_SUCCESS_ROLE_ID: int = config.getint("AuthConfig", "verification_success_role_id")
"""