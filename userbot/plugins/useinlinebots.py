#Inspired and Help Taken by Animesticker plugin("waifu" command)
# Plugin Made By @Anonymous_Machinee
# Kang With Credit
# (c) Phantom Userbot

## ALL IMPORTS ARE OF WAIFU PLUGIN (NO DELETION , ONLY ADDITION IN IMPORT)
from asyncio import sleep
from random import choice, getrandbits, randint
import re
from re import sub
from telethon import errors
import random
from os import execl
from telethon import events
from userbot import bot
import sys
import io
import html
from telethon.errors import ChatSendStickersForbiddenError
import json
from PIL import ImageEnhance, ImageOps
from userbot import CMD_HELP
from userbot.utils import phantom_cmd, sudo_cmd
from userbot.events import register
from telethon.tl.functions.messages import GetInlineBotResultsRequest

@borg.on(phantom_cmd(pattern="^.stic ?(.*)"))
@borg.on(sudo_cmd(pattern="^.stic ?(.*)", allow_sudo=True))
async def machine(stick):
#"""Creates random anime sticker!"""
    text = stick.pattern_match.group(1)
    if text is None:
        await event.edit("Use This Command as `.stic <emoji>`")
    stickers = await bot.inline_query(
        "sticker", f"{text}")
    hm=len(stickers)
    op=random.randrange(0,hm)
    try:
        await stickers[op].click(stick.chat_id,
                            reply_to=stick.reply_to_msg_id,
                            silent=True if stick.is_reply else False,
                            hide_via=True)
        await stick.delete()
    except ValueError:
    	await stick.edit("**Use This Command as** `.stic <any emoji>`\nor Stickers are Not Avaliable for Entered Emoji")
    except ChatSendStickersForbiddenError:
    	await stick.edit("Sorry boss Can't Send Sticker Here !!")

    
@borg.on(phantom_cmd(pattern="^.gogl ?(.*)"))
@borg.on(sudo_cmd(pattern="^.gogl ?(.*)", allow_sudo=True))
async def google(gogl):
#"""Creates random anime sticker!"""
    text = gogl.pattern_match.group(1)
    if text is None:
        await event.edit("Use This Command as `.gogl <Search Query>`")
    photo = await bot.inline_query(
        "goglimgbot", f"{text}")
    hm=len(photo)
    op=random.randrange(3,hm)
    ol = random.randrange(3,hm)
    try:
        await photo[0].click(gogl.chat_id,
                            reply_to=gogl.reply_to_msg_id,
                            silent=True if gogl.is_reply else False,
                            hide_via=True)
        await photo[1].click(gogl.chat_id,
                            reply_to=gogl.reply_to_msg_id,
                            silent=True if gogl.is_reply else False,
                            hide_via=True)
        await photo[2].click(gogl.chat_id,
                            reply_to=gogl.reply_to_msg_id,
                            silent=True if gogl.is_reply else False,
                            hide_via=True)        
        await photo[op].click(gogl.chat_id,
                            reply_to=gogl.reply_to_msg_id,
                            silent=True if gogl.is_reply else False,
                            hide_via=True)
        await photo[op].click(gogl.chat_id,
                            reply_to=gogl.reply_to_msg_id,
                            silent=True if gogl.is_reply else False,
                            hide_via=True)        
        await gogl.delete()
    except ValueError:
    	await gogl.edit("**Use This Command as** `.gogl <Search Query>`")

                
        
    CMD_HELP.update({
    'stic':
    ".stic : will send random sticker from emoji."
})
    CMD_HELP.update({
    'gogl':
    ".gogl : will Search Images and Send to The Chat"
})
