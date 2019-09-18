import inspect
import traceback
import asyncio
import sys
import io
import pyrogram
from pyrogram import Filters, Client
from pyrouserbot.deldog import haste, paste
from pyrouserbot import app, cmd

@app.on_message(Filters.command(["eval"],cmd) & Filters.me)
async def ev_al(client, message):
      cmd = message.text.split(" ", maxsplit=1)[1]
      reply_to_id = message.message_id
      if message.reply_to_message:
        reply_to_id = message.reply_to_message.message_id
      
      old_stderr = sys.stderr
      old_stdout = sys.stdout
      redirected_output = sys.stdout = io.StringIO()
      redirected_error = sys.stderr = io.StringIO()
      stdout, stderr, exc = None, None, None
      
      try:
         await aexec(cmd, message)
      except Exception:
         exc = traceback.format_exc()
      
      stdout = redirected_output.getvalue()
      stderr = redirected_error.getvalue()
      sys.stdout = old_stdout
      sys.stderr = old_stderr
      
      evaluation = ""
      if exc:
            evaluation = exc
      elif stderr:
            evaluation = stderr
      elif stdout:
            evaluation = stdout
      else:
            evaluation = "Success"
            
      final_output = "**EVAL**: `{}` \n\n **OUTPUT**: \n`{}` \n".format(cmd, evaluation)
      if len(final_output) > 4096:
         LINK=haste(final_output)
         await message.edit(LINK)
      else:
         await message.edit(final_output)
      
      
      
      
      
async def aexec(code, message):
    exec(
        f'async def __aexec(message): ' +
        ''.join(f'\n {l}' for l in code.split('\n'))
    )
    return await locals()['__aexec'](message)

