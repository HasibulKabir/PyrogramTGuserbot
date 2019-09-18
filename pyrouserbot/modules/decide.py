import pyrogram, requests
from pyrogram import Filters, Client
from pyrouserbot import app, cmd
from datetime import datetime
@app.on_message(Filters.command(["decide"], cmd) & Filters.me)
async def de_cide(client, message):
      message_id = message.message_id
      if message.reply_to_message:
         message_id = message.reply_to_message.message_id
      JSON = requests.get("https://yesno.wtf/api").json()
      await message.reply_animation(
            animation=JSON["image"],
            caption=JSON["answer"],
            reply_to_message_id=message_id
      )
      await message.delete()
      
