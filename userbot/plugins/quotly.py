#port to DARK COBRA by @hellboi-atul

import datetime
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from userbot import bot, CMD_HELP
from userbot.utils import phantom_cmd, sudo_cmd, edit_or_reply

#@register(outgoing=True, pattern="^.q(?: |$)(.*)")
@borg.on(phantom_cmd(pattern=r"qbot(?: |$)(.*)"))
@borg.on(sudo_cmd(pattern=r"qbot(?: |$)(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return 
    if not event.reply_to_msg_id:
       await edit_or_reply(event,"```Reply to any user message.```")
       return
    reply_message = await event.get_reply_message() 
    if not reply_message.text:
       await edit_or_reply(event,"```Reply to text message```")
       return
    chat = "@QuotLyBot"
    sender = reply_message.sender
    hitler = await edit_or_reply(event,"```Making a Quote```")
    async with bot.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=1031952739))
              await bot.forward_messages(chat, reply_message)
              response = await response 
          except YouBlockedUserError: 
              await event.reply("```Please unblock @QuotLyBot and try again```")
              return
          if response.text.startswith("Hi!"):
             await hitler.edit("```Can you kindly disable your forward privacy settings for good?```")
          else: 
             await hitler.delete()   
             await bot.forward_messages(event.chat_id, response.message)
