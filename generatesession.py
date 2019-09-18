################################
    # pip install pyrogram 
    # mainly for termux
################################
import os
try:
    import pyrogram
    from pyrogram import Client
except:
    os.system("pip install --upgrade pyrogram")
    import pyrogram
    from pyrogram import Client


APP_ID = input("Enter your APP_ID : ")
API_HASH = input("Enter your API_HASH : ")

app = Client(
             "pyrouserbot",
             api_id=APP_ID,
             api_hash=API_HASH
      )
with app:
     print(app.export_session_string())
