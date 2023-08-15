import asyncio
import random

from pyrogram.raw.functions.messages import DeleteHistory

from PyroUbot import extract_user, send_message


async def sg_cmd(client, message):
    get_user = await extract_user(message)
    lol = await send_message(message, "<b>ᴍᴇᴍᴘʀᴏsᴇs. . .</b>")

    if not get_user:
        return await lol.edit("<b>ᴜsᴇʀ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ</b>")

    try:
        get = await client.get_users(get_user)
        user_id = get.id
        name = f"{get.first_name} {get.last_name or ''}"
    except Exception as e:
        return await lol.edit(str(e))

    bot = ["@Sangmata_bot", "@SangMata_beta_bot"]
    getbot = random.choice(bot)

    await client.unblock_user(getbot)
    txt = await client.send_message(getbot, str(user_id))
    await asyncio.sleep(4)
    await txt.delete()
    await lol.delete()

    sg_name = [name.text async for name in client.search_messages(getbot, limit=2)]
    sg_name.reverse()

    for history in sg_name:
        if not history:
            await send_message(
                message, f"❌ {getbot} ᴛɪᴅᴀᴋ ᴅᴀᴘᴀᴛ ᴍᴇʀᴇsᴘᴏɴ ᴘᴇʀᴍɪɴᴛᴀᴀɴ", quote=True
            )
        else:
            await send_message(message, history.replace(str(user_id), name), quote=True)

    user_info = await client.resolve_peer(getbot)
    return await client.invoke(DeleteHistory(peer=user_info, max_id=0, revoke=True))
