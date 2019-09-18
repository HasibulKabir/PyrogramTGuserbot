import pyrogram, json
from pyrouserbot import app, cmd
from pyrogram import Filters, Client
from pyrouserbot.deldog import paste

@app.on_message(Filters.command(["json"],cmd) & Filters.me)
async def js_os(client, message):
      if message.reply_to_message:
         text=message.reply_to_message
      else:
         text=message
      if len(str(text)) > 4050:
            LINK = paste(text)
            await message.edit(LINK)
            return
      else:
            await message.edit("Json: \n`{}`".format(text))
      
