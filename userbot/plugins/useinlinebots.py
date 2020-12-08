# Inspired and Help Taken by Animesticker plugin("waifu" command)
# Plugin Made By @Anonymous_Machinee
# Kang With Credit
# (c) Phantom Userbot
# ALL IMPORTS ARE OF WAIFU PLUGIN (NO DELETION , ONLY ADDITION IN IMPORT)
import html
import io
import json
import random
import re
import sys
from asyncio import sleep
from os import execl
from random import choice
from random import getrandbits
from random import randint
from re import sub

from PIL import ImageEnhance
from PIL import ImageOps
from telethon import errors
from telethon import events
from telethon.errors import ChatSendInlineForbiddenError
from telethon.errors import ChatSendStickersForbiddenError
from telethon.tl.functions.messages import GetInlineBotResultsRequest

from userbot import bot
from userbot import CMD_HELP
from userbot.events import register
from userbot.utils import phantom_cmd
from userbot.utils import sudo_cmd

# @borg.on(phantom_cmd(pattern="^.stic ?(.*)"))
# @borg.on(sudo_cmd(pattern="^.stic ?(.*)", allow_sudo=True))


@register(outgoing=True, pattern="^.stic ?(.*)")  # Kang With Credit
async def machine(stick):
    # """Creates random anime sticker!"""
    text = stick.pattern_match.group(1)
    if text is None:
        await event.edit("Use This Command as `.stic <emoji>`")
    stickers = await bot.inline_query("sticker", f"{text}")
    hm = len(stickers)
    op = random.randrange(0, hm)
    try:
        await stickers[op].click(
            stick.chat_id,
            reply_to=stick.reply_to_msg_id,
            silent=True if stick.is_reply else False,
            hide_via=True,
        )
        await stick.delete()
    except ValueError:
        await stick.edit(
            "**Use This Command as** `.stic <any emoji>`\nor Stickers are Not Avaliable for Entered Emoji"
        )
    except ChatSendStickersForbiddenError:
        await stick.edit("Sorry boss, I can't send Sticker Here !!")


# Phantomot
# @Anonymous_Machinee


@register(outgoing=True, pattern="^.gqbot ?(.*)")  # Kang With Credit
async def phantomot(quote):
    # give quotes according to search # Thanks to SpecHide's GoodQuoteBot
    text = quote.pattern_match.group(1)
    if text is None:
        await event.edit("Use This Command as `.gqbot <search query>`")
    quotes = await bot.inline_query("GoodQuoteBot", f"{text}")
    hm = len(quotes)
    op = random.randrange(0, hm)  # Phantomot
    try:
        await quotes[op].click(
            quote.chat_id,
            reply_to=quote.reply_to_msg_id,
            silent=True if quote.is_reply else False,
            hide_via=True,
        )
        await quote.delete()
    except ValueError:
        await quote.edit("**Use This Command as** `.gqbot <author name>`")
    except ChatSendInlineForbiddenError:
        await quote.edit("Sorry boss, cant make inline request here !!")

    CMD_HELP.update({"stic": ".stic : will send random sticker from emoji."})
    CMD_HELP.update({
        "gqbot":
        ".gqbot : use this as .gqbot <author name>. Send Quoted Related to Search."
    })
