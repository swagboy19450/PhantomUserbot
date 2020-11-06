## Plugin for PHANTOM USERBOT
# Kang with Permission
# Ask in @PhantomSupport

# (C) Phantom Userbot

#""USAGE:= SEND a Random Quote from @Quotery Channel""
# command = .quotery #
# no of pics = 40 # 
# Please Bother to Update the Number of Pics#

import asyncio
import random
from re import sub
from random import choice
from telethon import events, functions
from userbot.utils import admin_cmd

QUOTES_COLLECTION = ("https://telegra.ph/file/31cf7484892cfdf85415f.jpg",
"https://telegra.ph/file/7408561005781ae9125ed.jpg",
"https://telegra.ph/file/18cd647447ad8421a7923.jpg",
"https://telegra.ph/file/6f18699851d78be60c9dc.jpg",
"https://telegra.ph/file/80073f27cd8dcccb55cc8.jpg",
"https://telegra.ph/file/04d7ebd5657a388514753.jpg",
"https://telegra.ph/file/f3fe1b4d5623dadb8fdc6.jpg",
"https://telegra.ph/file/ad5b030e5596c1a1eea03.jpg",
"https://telegra.ph/file/758dfac8d5061c0660cbb.jpg",
"https://telegra.ph/file/56f439a2b533dfa8373d7.jpg",
"https://telegra.ph/file/8632fd0f1ee5dddf02027.jpg",
"https://telegra.ph/file/7f7872d89a5573746bd34.jpg",
"https://telegra.ph/file/d2445817e0b103b939aed.jpg",
"https://telegra.ph/file/cddb7e77e4082a4a0be52.jpg",
"https://telegra.ph/file/b8eb7f9a41241bae0cea0.jpg",
"https://telegra.ph/file/b92050d05c10f4680f1aa.jpg",
"https://telegra.ph/file/82e4634de56da033509a0.jpg",
"https://telegra.ph/file/c18f58061dd536503c4b5.jpg",
"https://telegra.ph/file/18ca367663225c40a8cbb.jpg",
"https://telegra.ph/file/098207c0f7079caec1c23.jpg",
"https://telegra.ph/file/48ee775b12239a2a986a9.jpg",
"https://telegra.ph/file/367a368af7fbdb3aa53c3.jpg",
"https://telegra.ph/file/906934141e7a8d4258261.jpg",
"https://telegra.ph/file/6ec6810e2b0fedca4cf01.jpg",
"https://telegra.ph/file/7c8b043ce1067d92c1916.jpg",
"https://telegra.ph/file/1457f66f729cedfcee07a.jpg",
"https://telegra.ph/file/0a87339240a7976e46496.jpg",
"https://telegra.ph/file/73b4a376c0fb1a1f6f609.jpg",
"https://telegra.ph/file/8ba0f1cec5c812937f040.jpg",
"https://telegra.ph/file/0f9f34902eb3573fd5952.jpg",
"https://telegra.ph/file/d37b8ebfe14136f84586c.jpg",
"https://telegra.ph/file/f993f3f80071dd390eb0e.jpg",
"https://telegra.ph/file/c4ebecede33be6e1c0da0.jpg",
"https://telegra.ph/file/e8639396eca652baad053.jpg",
"https://telegra.ph/file/2e1b67d21fede429a9b17.jpg",
"https://telegra.ph/file/1be71e60aa29aae1f1fe7.jpg",
"https://telegra.ph/file/2ff07b757875aac453a54.jpg",
"https://telegra.ph/file/3ec4e4b017194be65ace7.jpg",
"https://telegra.ph/file/0b1ddef4d9d0947b10785.jpg",
"https://telegra.ph/file/6b6652a5a5ef3456a180b.jpg",
) #PHANTOMOT


@borg.on(admin_cmd(pattern=f"quotery$", outgoing=True))
async def _(event):
    QUOTE = random.choice(QUOTES_COLLECTION)   
    await borg.send_file(event.chatid,file=QUOTE)
    await event.delete()
