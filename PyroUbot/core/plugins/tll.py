import asyncio
from random import shuffle

tagallgcid = []
import random

emoji_categories = {
    'smileys': ['😀', '😃', '😄', '😁', '😆', '😅', '😂', '🤣', '😊', '😍', '🥰', '😘', '😎', '🥳'],
    'animals': ['🐶', '🐱', '🐰', '🐻', '🐼', '🦁', '🐸', '🦊', '🦔', '🦄', '🐢', '🐠', '🐦', '🦜'],
    'food': ['🍎', '🍕', '🍔', '🍟', '🍩', '🍦', '🍓', '🥪', '🍣', '🍔', '🍕', '🍝', '🍤', '🥗'],
    'nature': ['🌲', '🌺', '🌞', '🌈', '🌊', '🌍', '🍁', '🌻', '🌸', '🌴', '🌵', '🍃', '🍂', '🌼'],
    'travel': ['✈️', '🚀', '🚲', '🚗', '⛵', '🏔️', '🚁', '🚂', '🏍️', '🚢', '🚆', '🛴', '🛸', '🛶'],
    'sports': ['⚽', '🏀', '🎾', '🏈', '🎱', '🏓', '🥊', '⛳', '🏋️', '🏄', '🤸', '🏹', '🥋', '🛹'],
}

def emoji_random():
     random_category = random.choice(list(emoji_categories.keys()))
     return random.choice(emoji_categories[random_category])


async def tagall_cmd(client, message):
    if message.chat.id in tagallgcid:
        return
    tagallgcid.append(message.chat.id)
    text = message.text.split(None, 1)[1] if len(message.text.split()) != 1 else ""
    users = [
        f"<a href=tg://user?id={member.user.id}>{random_emoji()}</a>"
        async for member in message.chat.get_members()
        if not (member.user.is_bot or member.user.is_deleted)
    ]
    shuffle(users)
    m = message.reply_to_message or message
    for output in [users[i : i + 5] for i in range(0, len(users), 5)]:
        if message.chat.id not in tagallgcid:
            break
        await asyncio.sleep(1.5)
        await m.reply_text(
            text + "\n\n" + ", ".join(output), quote=bool(message.reply_to_message)
        )
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
