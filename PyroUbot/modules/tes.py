import random
from PyroUbot import *

@PY.UBOT("tes")
async def _(client, message):
    react = "🐳 🎄🦄 ☃️".split()
    for x in client._ubot:
        await x.send_reaction(message.chat.id, message.id, random.choice(react))
