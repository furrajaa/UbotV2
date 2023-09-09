import asyncio
from random import shuffle
from PyroUbot import *
tagallgcid = []


async def tagall_cmd(client, message):
    if message.chat.id in tagallgcid:
        return
    tagallgcid.append(message.chat.id)
    text = message.text.split(None, 1)[1] if len(message.text.split()) != 1 else ""
    users = [
        f"<a href=tg://user?id={member.user.id}>{generate_random_emoji()}</a>"
        async for member in message.chat.get_members()
        if not (member.user.is_bot or member.user.is_deleted)
    ]
    shuffle(users)
    m = message.reply_to_message or message
    for output in [users[i : i + 5] for i in range(0, len(users), 5)]:
        if message.chat.id not in tagallgcid:
            break
        await m.reply_text(
            f"{text}\n\n{' '.join(output)}", quote=bool(message.reply_to_message)
        )
        await asyncio.sleep(2)
    try:
        tagallgcid.remove(message.chat.id)
    except Exception:
        pass


async def batal_cmd(client, message):
    if message.chat.id not in tagallgcid:
        return await message.reply_text(
            "sedang tidak ada perintah: <code>tagall</code> yang digunakan"
        )
    try:
        tagallgcid.remove(message.chat.id)
    except Exception:
        pass
    await message.reply_text("ok tagall berhasil dibatalkan")
