from PyroUbot import *

__MODULE__ = "asupan"
__HELP__ = """
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴀsᴜᴘᴀɴ 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}asupan</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢɪʀɪᴍ ᴠɪᴅᴇᴏ ᴀsᴜᴘᴀɴ ʀᴀɴᴅᴏᴍ

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}cewek</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢɪʀɪᴍ ᴘʜᴏᴛᴏ ᴄᴇᴡᴇᴋ ʀᴀɴᴅᴏᴍ

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}cowok</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢɪʀɪᴍ ᴘʜᴏᴛᴏ ᴄᴏᴡᴏᴋ ʀᴀɴᴅᴏᴍ

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}anime</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢɪʀɪᴍ ᴘʜᴏᴛᴏ ᴀɴɪᴍᴇ ʀᴀɴᴅᴏᴍ
"""


@PY.UBOT("asupan")
async def _(client, message):
    await video_asupan(client, message)


@PY.UBOT("hentai")
async def _(client, message):
    await waifu_cmf(client, message)


@PY.UBOT("cewek")
async def _(client, message):
    await photo_cewek(client, message)


@PY.UBOT("cowok")
async def _(client, message):
    await photo_cowok(client, message)


@PY.UBOT("anime")
async def _(client, message):
    await photo_anime(client, message)
