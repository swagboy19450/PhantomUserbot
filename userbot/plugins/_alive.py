# Thanks to Sipak bro and Aryan.. 
# animation Idea by @NOOB_GUY_OP (Sipakisking) && @Hell boy_pikachu
# Made by @hellboi_atul ....and thanks to @Crackexy for the logos...
# Kang with credits else gay...
import asyncio
import random
from telethon import events
from userbot.utils import admin_cmd
from userbot import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Unknown"

PHANTOM_IMG="https://telegra.ph/file/c7b627350ba5322b6d75d.jpg"

pm_caption = "**PHANTOM USERBOT IS ONLINE**\n"
pm_caption += f"**My Master** => {DEFAULTUSER}\n\n"
pm_caption += "🤖 **SYSTEM INFO** 🤖\n"
pm_caption += "**ᴛᴇʟᴇᴛʜᴏɴ - ᴠᴇʀsɪᴏɴ ---->**15.0.0\n"
pm_caption += "**ᴘʏᴛʜᴏɴ -  ᴠᴇʀsɪᴏɴ ------>**3.8.5\n\n"
pm_caption += "**🌀 SUPPORT INFO 🌀**\n"
pm_caption += "**sᴜᴘᴘᴏʀᴛ - ᴄʜᴀɴɴᴇʟ ---->** [PhantomOt](https://t.me/PhantomOt)\n"
pm_caption += "**sᴜᴘᴘᴏʀᴛ - ɢʀᴏᴜᴘ =** [PhantomSupport](https://t.me/PhantomSupport)\n\n"
pm_caption += f"[❤️ Deploy your own PHANTOM USERBOT ❤️](https://bit.ly/deployphantom)"

@borg.on(admin_cmd(pattern=r"alive"))
async def amireallyalive(alive):
    chat = await alive.get_chat()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id,file=PHANTOM_IMG,caption=pm_caption)
    await alive.delete()
