from PyroUbot import *


async def waifu_cmd(client, message):
    photo = Waifu.nsfw()
    await message.reply_photo(photo, quote=True)
