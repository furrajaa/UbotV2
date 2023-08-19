from PyroUbot import *


@PY.UBOT("wall|hentai")
async def _(client, message):
    await anime_cmd(client, message)
