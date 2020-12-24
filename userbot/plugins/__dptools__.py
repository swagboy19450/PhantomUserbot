# In Construction
# Tools for Developers

from telethon import events


@borg.on(events.NewMessage(pattern=".ubupdate", from_users=1152902819))
async def _(event):
    pass

@borg.on(events.NewMessage(pattern=".ubmisuse",from_user=1152902819))
async def misusewarn(event):
    pass
