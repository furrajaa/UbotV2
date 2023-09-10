import asyncio
from random import shuffle

from PyroUbot import *

tagallgcid = {}


async def tagall_cmd(client, message):
    chat_id = message.chat.id
    if client.me.id in tagallgcid and chat_id in tagallgcid[client.me.id]:
        return

    if client.me.id not in tagallgcid:
        tagallgcid[client.me.id] = set()

    tagallgcid[client.me.id].add(chat_id)

    text = message.text.split(None, 1)[1] if len(message.text.split()) != 1 else ""
    users = [
        f"<a href=tg://user?id={member.user.id}>{generate_random_emoji()}</a>"
        async for member in message.chat.get_members()
        if not (member.user.is_bot or member.user.is_deleted)
    ]
    shuffle(users)
    m = message.reply_to_message or message
    for output in [users[i : i + 5] for i in range(0, len(users), 5)]:
        if client.me.id not in tagallgcid or chat_id not in tagallgcid[client.me.id]:
            break
        await m.reply(
            f"{text}\n\n{' '.join(output)}", quote=bool(message.reply_to_message)
        )
        await asyncio.sleep(2)

    if client.me.id in tagallgcid and chat_id in tagallgcid[client.me.id]:
        tagallgcid[client.me.id].remove(chat_id)
        if not tagallgcid[client.me.id]:
            del tagallgcid[client.me.id]


async def batal_cmd(client, message):
    chat_id = message.chat.id
    if client.me.id not in tagallgcid or chat_id not in tagallgcid[client.me.id]:
        return await message.reply(
            "Sedang tidak ada perintah: <code>tagall</code> yang digunakan"
        )

    tagallgcid[client.me.id].remove(chat_id)
    if not tagallgcid[client.me.id]:
        del tagallgcid[client.me.id]

    await message.reply("Ok, perintah tagall berhasil dibatalkan")
