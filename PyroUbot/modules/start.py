from .. import *


@PY.BOT("start")
async def _(client, message):
    await start_cmd(client, message)
