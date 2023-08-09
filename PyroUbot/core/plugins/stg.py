import re

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
            parsed_prefix = re.sub(
                r"([\U0001F1E0-\U0001F1FF])", r"<b>\1</b>", parsed_prefix
            )
            return await Tm.edit(f"<b>✅ ᴘʀᴇғɪx ᴛᴇʟᴀʜ ᴅɪᴜʙᴀʜ ᴋᴇ: {parsed_prefix}</b>")
        except Exception as error:
            return await Tm.edit(str(error))
