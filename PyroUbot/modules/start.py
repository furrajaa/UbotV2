from .. import *


@PY.BOT("start")
async def _(client, message):
    await start_cmd(client, message)

@PY.UBOT("ping")
async def _(client, message):
    await ping_cmd(client, message)
