import datetime
from pyrogram import Client
from time import time

from PyroUbot import *


async def ping_cmd(client, message):
    ub_uptime = await get_uptime(client.me.id)
    uptime = await get_time((time() - ub_uptime))
    start = datetime.now()
    await client.send_message(message.chat.id, "🏓 Pong!")
    end = datetime.now()
    delta_ping = (end - start).microseconds / 1000
    emot_pong = await get_vars(client.me.id, "EMOJI_PING_PONG") or "5269563867305879894"
    emot_uptime = await get_vars(client.me.id, "EMOJI_UPTIME") or "5316615057939897832"
    emot_mention = await get_vars(client.me.id, "EMOJI_MENTION") or "6226371543065167427"
    if client.me.is_premium:
        _ping = f"""
<b><emoji id={emot_pong}>🏓</emoji> Pong:</b> <code>{str(delta_ping).replace('.', ',')} ms</code>
<b><emoji id={emot_uptime}>⏰</emoji> Uptime:</b> <code>{uptime}</code>
<b><emoji id={emot_mention}>👑</emoji> Mention:</b> <a href=tg://user?id={client.me.id}>{client.me.first_name} {client.me.last_name or ''}</a>
"""
    else:
        _ping = f"""
<b>❏ Pong:</b> <code>{str(delta_ping).replace('.', ',')} ms</code>
<b>├ Uptime:</b> <code>{uptime}</code>
<b>╰ Mention:</b> <a href=tg://user?id={client.me.id}>{client.me.first_name} {client.me.last_name or ''}</a>
"""
    await message.reply_text(_ping)

@PY.UBOT("ping")
async def _(client, message):
    await ping_cmd(client, message)
