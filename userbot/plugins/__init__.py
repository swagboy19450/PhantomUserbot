from userbot import darkdef
from userbot import OWNER_ID
from telethon.tl.functions.users import GetFullUserRequest

darkmusic = darkdef.darkmusic 
darkmusicvideo = darkdef.darkmusicvideo

async def extrafec(event):
  ok = await event.client(GetFullUserRequest(OWNER_ID))
  owner_name = f"{ok.user.first_name} {ok.user.last_name}"
  return owner_name
    

