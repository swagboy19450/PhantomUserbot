from telethon import events
import asyncio
from userbot.utils import phantom_cmd, sudo_cmd
from userbot.utils import edit_or_reply as eor

         
@borg.on(phantom_cmd(pattern="repo"))
@borg.on(phantom_cmd(pattern="repo", allow_sudo = True))
async def source(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("**Here is the repo of **[PHANTOM USERBOT ](https://github.com/prothinkergang/phantomuserbot)")
