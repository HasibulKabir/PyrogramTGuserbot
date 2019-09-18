import pyrogram
from pyrogram import Filters, Client
from pyrouserbot import app, cmd
from datetime import datetime

@app.on_message(Filters.command(["ping"],cmd) & Filters.me)
async def pi_ng(client, message):
      start = datetime.now()
      await message.edit("Pong!")
      end = datetime.now()
      ms = (end - start).microseconds / 1000
      await message.edit("Pong!\n{} ms".format(ms))
      
