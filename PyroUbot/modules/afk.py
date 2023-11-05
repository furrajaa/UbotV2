"create by: NorSodikin.t.me"
"requests by: Bocil-Userbot"


from time import time

from PyroUbot import *

__MODULE__ = "afk"
__HELP__ = """
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴀғᴋ 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}afk</code></code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢᴀᴋᴛɪғᴋᴀɴ ᴀғᴋ 

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}unafk</code></code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴᴏɴᴀᴋᴛɪғᴋᴀɴ ᴀғᴋ
"""


class AFK:
    def __init__(self, client, message, reason=""):
        self.client = client
        self.message = message
        self.reason = reason

    async def set_afk(self):
        db_afk = {"time": time(), "reason": self.reason}
        msg_afk = (
            f"<b>❏ sᴇᴅᴀɴɢ ᴀғᴋ\n ╰ ᴀʟᴀsᴀɴ: {self.reason}</b>"
            if self.reason
            else "<b>❏ sᴇᴅᴀɴɢ ᴀғᴋ</b>"
        )
        await set_vars(self.client.me.id, "AFK", db_afk)
        await self.message.reply(msg_afk)
        return await self.message.delete()

    async def get_afk(self):
        vars = await get_vars(self.client.me.id, "AFK")
        if vars:
            afk_time = vars.get("time")
            afk_reason = vars.get("reason")
            afk_runtime = await get_time(time() - afk_time)
            afk_text = (
                f"<b>❏ sᴇᴅᴀɴɢ ᴀғᴋ\n ├ ᴡᴀᴋᴛᴜ: {afk_runtime}\n ╰ ᴀʟᴀsᴀɴ: {afk_reason}</b>"
                if afk_reason
                else f"<b>❏ sᴇᴅᴀɴɢ ᴀғᴋ\n ╰ ᴡᴀᴋᴛᴜ: {afk_runtime}</b>"
            )
            return await self.message.reply(afk_text)

    async def unset_afk(self):
        vars = await get_vars(self.client.me.id, "AFK")
        if vars:
            afk_time = vars.get("time")
            afk_runtime = await get_time(time() - afk_time)
            afk_text = f"<b>❏ ᴋᴇᴍʙᴀʟɪ ᴏɴʟɪɴᴇ\n ╰ ᴀғᴋ sᴇʟᴀᴍᴀ: {afk_runtime}"
            await self.message.reply(afk_text)
            await self.message.delete()
            return await remove_vars(self.client.me.id, "AFK")


@PY.UBOT("afk")
async def _(client, message):
    reason = get_arg(message)
    afk_handler = AFK(client, message, reason)
    await afk_handler.set_afk()


@PY.AFK()
async def _(client, message):
    afk_handler = AFK(client, message)
    await afk_handler.get_afk()


@PY.UBOT("unafk")
async def _(client, message):
    afk_handler = AFK(client, message)
    return await afk_handler.unset_afk()
