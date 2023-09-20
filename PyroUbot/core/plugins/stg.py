from PyroUbot import *


async def setprefix(client, message):
    Tm = await message.reply("ᴍᴇᴍᴘʀᴏsᴇs...", quote=True)
    if len(message.command) < 2:
        return await Tm.edit(f"<code>{message.text}</code> sɪᴍʙᴏʟ ᴘʀᴇғɪx")
    else:
        ub_prefix = []
        for prefix in message.command[1:]:
            if prefix.lower() == "none":
                ub_prefix.append("")
            else:
                ub_prefix.append(prefix)
        try:
            ubot.set_prefix(message.from_user.id, ub_prefix)
            await set_pref(message.from_user.id, ub_prefix)
            parsed_prefix = " ".join(f"<code>{prefix}</code>" for prefix in ub_prefix)
            return await Tm.edit(f"<b>✅ ᴘʀᴇғɪx ᴛᴇʟᴀʜ ᴅɪᴜʙᴀʜ ᴋᴇ: {parsed_prefix}</b>")
        except Exception as error:
            return await Tm.edit(str(error))


async def change_emot(client, message):
    try:
        msg = await message.reply("ᴍᴇᴍᴘʀᴏsᴇs...", quote=True)

        if not client.me.is_premium:
            return await msg.edit(
                "<b>ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴀᴛ ᴘᴇʀɪɴᴛᴀʜ ɪɴɪ ᴀᴋᴜɴ ᴀɴᴅᴀ ʜᴀʀᴜs ᴘʀᴇᴍɪᴜᴍ ᴛᴇʀʟᴇʙɪʜ ᴅᴀʜᴜʟᴜ</b>"
            )

        if len(message.command) < 3:
            return await msg.edit("<b>ᴛᴏʟᴏɴɢ ᴍᴀsᴜᴋᴋᴀɴ ǫᴜᴇʀʏ ᴅᴀɴ ᴠᴀʟᴇᴜ ɴʏᴀ</b>")

        query_mapping = {"pong": "EMOJI_PING_PONG", "uptime": "EMOJI_UPTIME"}
        command, mapping, value = message.command[:3]

        if mapping.lower() in query_mapping:
            query_var = query_mapping[mapping.lower()]
            emoji_id = None

            if message.entities:
                for x in message.entities:
                    if x.custom_emoji_id:
                        emoji_id = x.custom_emoji_id
                        continue

            if emoji_id:
                await set_vars(client.me.id, query_var, value)
                return await msg.edit(
                    f"<b>✅ <code>{query_var}</code> ʙᴇʀʜᴀsɪʟ ᴅɪ sᴇᴛᴛɪɴɢ ᴋᴇ:</b> <emoji id={emoji_id}>😎</emoji>"
                )
            else:
                return await msg.edit("<b>ᴛɪᴅᴀᴋ ᴅᴀᴘᴀᴛ ᴍᴇɴᴇᴍᴜᴋᴀɴ ᴇᴍᴏᴊɪ ᴘʀᴇᴍɪᴜᴍ</b>")

    except Exception as error:
        await msg.edit(str(error))
