import sys, importlib, asyncio

from pyrouserbot import __copy__, __version__, app, logger
from pyrouserbot.modules import ALL_MODULES
import pyrogram
from pyrogram import *

for module_name in ALL_MODULES:
    imported_module = importlib.import_module("pyrouserbot.modules." + module_name)

async def main():
        await app.start()
        logger.info(f"Your bot is Version {__version__}\n")
        await app.idle()
        print("\nUserbot Stopped\n")
if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
