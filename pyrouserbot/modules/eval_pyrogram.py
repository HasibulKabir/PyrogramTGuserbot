from pyrogram import Client, Filters
import time
from pyrouserbot.deldog import haste, paste
from pyrouserbot import app, cmd

RUNNING = "**Eval Expression:**\n```{}```\n**Running...**"
ERROR = "**Eval Expression:**\n```{}```\n**Error:**\n```{}```"
SUCCESS = "**Eval Expression:**\n```{}```\n**Success**"
RESULT = "**Eval Expression:**\n```{}```\n**Result:**\n```{}```"

@app.on_message(Filters.command("evp", cmd) & Filters.me)
async def eval_expression(client, message):
    expression = " ".join(message.command[1:])

    if expression:
        await message.edit(RUNNING.format(expression))
        time.sleep(2)
        try:
            result = await eval(expression)
        except Exception as e:
            await message.edit(ERROR.format(expression, e))
        else:
            if len(str(result)) > 4040:
               Paste = str(result)
               Paste = Paste[1:-1]
               LINK= haste(Paste)
               await message.edit(LINK)
            elif result is None:
               await message.edit(SUCCESS.format(expression))
            else:
                await message.edit(RESULT.format(expression, result))
