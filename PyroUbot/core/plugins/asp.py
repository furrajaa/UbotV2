import random

from pyrogram.enums import MessagesFilter


async def video_asupan(client, message):
    y = await message.reply_text("<b>🔍 ᴍᴇɴᴄᴀʀɪ ᴠɪᴅᴇᴏ ᴀsᴜᴘᴀɴ...</b>")
    try:
        asupannya = []
        async for asupan in client.search_messages(
            "@AsupanNyaSaiki", filter=MessagesFilter.VIDEO
        ):
            asupannya.append(asupan)
        video = random.choice(asupannya)
        await video.copy(message.chat.id, reply_to_message_id=message.id)
        await y.delete()
    except Exception as error:
        await y.edit(error)


async def photo_cewek(client, message):
    y = await message.reply_text("<b>🔍 ᴍᴇɴᴄᴀʀɪ ᴀʏᴀɴɢ...</b>")
    try:
        ayangnya = []
        async for ayang in client.search_messages(
            "@AyangSaiki", filter=MessagesFilter.PHOTO
        ):
            ayangnya.append(ayang)
        photo = random.choice(ayangnya)
        await photo.copy(message.chat.id, reply_to_message_id=message.id)
        await y.delete()
    except Exception as error:
        await y.edit(error)


async def photo_cowok(client, message):
    y = await message.reply_text("<b>🔍 ᴍᴇɴᴄᴀʀɪ ᴀʏᴀɴɢ...</b>")
    try:
        ayang2nya = []
        async for ayang2 in client.search_messages(
            "@Ayang2Saiki", filter=MessagesFilter.PHOTO
        ):
            ayang2nya.append(ayang2)
        photo = random.choice(ayang2nya)
        await photo.copy(message.chat.id, reply_to_message_id=message.id)
        await y.delete()
    except Exception as error:
        await y.edit(error)


async def photo_anime(client, message):
    y = await message.reply_text("<b>🔍 ᴍᴇɴᴄᴀʀɪ ᴀɴɪᴍᴇ...</b>")
    anime_channel = random.choice(["@animehikarixa", "@Anime_WallpapersHD"])
    try:
        animenya = []
        async for anime in client.search_messages(
            anime_channel, filter=MessagesFilter.PHOTO
        ):
            animenya.append(anime)
        photo = random.choice(animenya)
        await photo.copy(message.chat.id, reply_to_message_id=message.id)
        await y.delete()
    except Exception as error:
        await y.edit(error)


async def video_bokep(client, message):
    y = await message.reply_text("<b>🔍 ᴍᴇɴᴄᴀʀɪ ᴠɪᴅᴇᴏ ʙᴏᴋᴇᴘ...</b>")
    try:
        bokepnya = []
        async for bokep in client.search_messages(
            -1001867672427, filter=MessagesFilter.VIDEO
        ):
            bokepnya.append(bokep)
        video = random.choice(bokepnya)
        await video.copy(message.chat.id, reply_to_message_id=message.id)
        await y.delete()
    except Exception as error:
        await y.edit(error)
