from asyncio import sleep
from pyrogram import Client, filters

api_id = 
api_hash = ""

app = Client("my_account", api_id, api_hash)
spam_text = 'Путін хуйло'
delay = 0.1 #100ms


@app.on_message(filters.command('spam', prefixes='.') & filters.me)
async def enable_spam(_, message):
    await message.delete()
    cmd = message.text.split()
    for i in range(int(cmd[1])):
        await message.reply_text(spam_text)
        await sleep(delay)

app.run()