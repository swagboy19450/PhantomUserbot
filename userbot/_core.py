import asyncio
import os
import requests
from requests import exceptions, get
from datetime import datetime
from pathlib import Path
from telethon.tl.types import InputMessagesFilterDocument
from userbot.utils import phantom_cmd, load_module, remove_plugin
from userbot import ALIVE_NAME
from userbot import bot
from userbot.utils import edit_or_reply
from telethon.errors import ChatSendMediaForbiddenError
DELETE_TIMEOUT = 5
thumb_image_path = "./Resources/phantomot.jpg"
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Unknown"


@bot.on(phantom_cmd(pattern=r"send (?P<shortname>\w+)", outgoing=True))
async def send(event):
    if event.fwd_from:
        return
    hmm = bot.uid
    message_id = event.message.id
    thumb = thumb_image_path
    input_str = event.pattern_match.group(1)
    the_plugin_file = "./userbot/plugins/{}.py".format(input_str)
    if os.path.exists(the_plugin_file):
        try:
            start = datetime.now()
            pro = await event.client.send_file(
            event.chat_id,
            the_plugin_file,
            force_document=True,
            allow_cache=False,
            thumb=thumb,
            reply_to=message_id)
            end = datetime.now()
            time_taken_in_ms = (end - start).seconds
            m_list = None
            with open(the_plugin_file, "rb") as fd:
                m_list = fd.readlines()
            message = ""
            for m in m_list:
                    message += m.decode("UTF-8") + "\r\n"
            url = "https://del.dog/documents"
            r = requests.post(url, data=message.encode("UTF-8")).json()
            url = f"https://del.dog/{r['key']}"
            await pro.edit(
                       f"**==> Plugin name :** `{input_str}`\n**==> Uploaded in {time_taken_in_ms} seconds only.**\n**==> Uploaded by :** [{DEFAULTUSER}](tg://user?id={hmm})\n==> **View on Web** : [Del-Dog]({url})"
        ) #doesnt work in saved messages
            await asyncio.sleep(1)
            await event.delete()
        except ChatSendMediaForbiddenError:
            await event.edit("Boss, Cant Send File Here")
            await asyncio.sleep(0.5)
            await event.edit("pasting the codes...")
            m_list = None
            with open(the_plugin_file, "rb") as fd:
                m_list = fd.readlines()
            message = ""
            for m in m_list:
                    message += m.decode("UTF-8") + "\r\n"
            url = "https://del.dog/documents"
            r = requests.post(url, data=message.encode("UTF-8")).json()
            url = f"https://del.dog/{r['key']}"
            await event.edit(f"Pasted `{input_str}` [Here]({url}) !!")
    else:
        await edit_or_reply(event, "**404**: __File Not Found__")


@bot.on(phantom_cmd(pattern="install"))
async def install(event):
    if event.fwd_from:
        return
    if event.reply_to_msg_id:
        try:
            downloaded_file_name = (
                await event.client.download_media(  # pylint:disable=E0602
                    await event.get_reply_message(),
                    "userbot/plugins/",  # pylint:disable=E0602
                )
            )
            if "(" not in downloaded_file_name:
                path1 = Path(downloaded_file_name)
                shortname = path1.stem
                load_module(shortname.replace(".py", ""))
                await event.edit(
                    "`{}` successfully installed\nJoin @Phantom_USERBOT".format(
                        os.path.basename(downloaded_file_name)
                    )
                )
            else:
                os.remove(downloaded_file_name)
                await event.edit(
                    "**Plugin cannot be installed or is pre-installed.**"
                )
        except Exception as e:  # pylint:disable=C0103,W0703
            await event.edit(str(e))
            os.remove(downloaded_file_name)
    await asyncio.sleep(DELETE_TIMEOUT)
    await event.delete()


@bot.on(phantom_cmd(pattern=r"unload (?P<shortname>\w+)$"))
async def unload(event):
    if event.fwd_from:
        return
    shortname = event.pattern_match["shortname"]
    try:
        remove_plugin(shortname)
        await event.edit(f"Successfully unloaded {shortname}")
    except Exception as e:
        await event.edit(
            "Successfully unloaded {shortname}\n{}".format(
                shortname, str(e)
            )
        )


@bot.on(phantom_cmd(pattern=r"load (?P<shortname>\w+)$"))
async def load(event):
    if event.fwd_from:
        return
    shortname = event.pattern_match["shortname"]
    try:
        try:
            remove_plugin(shortname)
        except BaseException:
            pass
        load_module(shortname)
        await event.edit(f"Successfully loaded {shortname}")
    except Exception as e:
        await event.edit(
            f"Sorry,{shortname} can not be loaded\nbecause of the following error.\n{str(e)}"
        )

