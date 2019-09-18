import os, sys, logging, importlib, asyncio
from pathlib import Path
from datetime import datetime
from pyrogram import Client, Filters

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.WARN)
logger = logging.getLogger(__name__)

__version__ = '0.1.0'
__author__ = 'Md. Hasibul Kobir'
__source__ = 'https://github.com/hasibulkabir/pyrouserbot'
__copyright__ = 'Copyright (c) 2019 ' + __author__
__copy__ = f"Pyrouserbot v{__version__}  {__copyright__}"

app = Client(
             session_name=os.environ.get("SESSION"),
             api_id=os.environ.get("API_ID"),
             api_hash=os.environ.get("API_HASH"),
             app_version=f"Pybogram v{__version__}"
      )

ISAFK = False
AFK_REASON = "No Reason"
START_TIME = datetime.now()
LOGGER_GROUP = os.environ.get("LGROUP")
LOG = True
cmd = ["#","!",".", "-"]
