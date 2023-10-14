# Copyright (c) 2022 Itz-fork

import os


class Config(object):
    APP_ID = int(os.environ.get("APP_ID", "29696092")
    API_HASH = os.environ.get("API_HASH", "58d9ba5b26ff3b50fbb811d64c077541")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6349196945:AAFOAo44j_y68OPYm3rL9VUfaY66Bc7MXfs")
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "5263032279").split())
    IS_PUBLIC_BOT = os.environ.get("IS_PUBLIC_BOT") in ["True", "true"]
    LOGS_CHANNEL = int(os.environ.get("LOGS_CHANNEL")) if os.environ.get("LOGS_CHANNEL") else None
    # DON'T CHANGE THESE 2 VARS
    DOWNLOAD_LOCATION = "./NexaBots"
    TG_MAX_SIZE = 2040108421
    # Mega User Account
    MEGA_EMAIL = os.environ.get("MEGA_EMAIL")
    MEGA_PASSWORD = os.environ.get("MEGA_PASSWORD")
