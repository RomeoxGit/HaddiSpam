from .. import Riz, Riz2, Riz3, Riz4, Riz5, Riz6, Riz7, Riz8, Riz9, Riz10, SUDO_USERS
from telethon import events
import os
import random
import sys


@Riz.on(events.NewMessage(pattern=".refresh"))
@Riz2.on(events.NewMessage(pattern=".refresh"))
@Riz3.on(events.NewMessage(pattern=".refresh"))
@Riz4.on(events.NewMessage(pattern=".refresh"))
@Riz5.on(events.NewMessage(pattern=".refresh"))
@Riz6.on(events.NewMessage(pattern=".refresh"))
@Riz7.on(events.NewMessage(pattern=".refresh"))
@Riz8.on(events.NewMessage(pattern=".refresh"))
@Riz9.on(events.NewMessage(pattern=".refresh"))
@Riz10.on(events.NewMessage(pattern=".refresh"))
async def refresh(e):
    if e.sender_id in SUDO_USERS:
        text = "𝖱𝖾𝖿𝗋𝖾𝗌𝗁𝗂𝗇𝗀.... 𝖠𝗇𝖽 𝖢𝗈𝗇𝗇𝖾𝖼𝗍𝗂𝗇𝗀 𝖳𝗈 𝖳𝗁𝖾 **𝘙𝘰𝘮𝘦𝘰'𝘴 𝘚𝘦𝘳𝘷𝘦𝘳** !! 𝖯𝗅𝗓 𝖶𝖺𝗂𝗍 𝖥𝗈𝗋 𝖥𝖾𝗐 𝖬𝗂𝗇𝗎𝗍𝖾𝗌 ✨"
        await e.reply(text, parse_mode=None, link_preview=None)
        try:
            await Riz.disconnect()
        except Exception:
            pass
        try:
            await Riz2.disconnect()
        except Exception:
            pass
        try:
            await Riz3.disconnect()
        except Exception:
            pass
        try:
            await Riz4.disconnect()
        except Exception:
            pass
        try:
            await Riz5.disconnect()
        except Exception:
            pass
        try:
            await Riz6.disconnect()
        except Exception:
            pass
        try:
            await Riz7.disconnect()
        except Exception:
            pass
        try:
            await Riz8.disconnect()
        except Exception:
            pass
        try:
            await Riz9.disconnect()
        except Exception:
            pass
        try:
            await Riz10.disconnect()
        except Exception:
            pass

        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()
