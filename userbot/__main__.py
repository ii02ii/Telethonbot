import glob
import os
import sys
from pathlib import Path

import telethon.utils
from telethon import TelegramClient

from userbot import LOGS, bot
from userbot.Config import Config
from userbot.utils import load_module


async def add_bot(bot_token):
    try:
        await bot.start(bot_token)
        bot.me = await bot.get_me()
        bot.uid = telethon.utils.get_peer_id(bot.me)
    except Exception as e:
        LOGS.error(f"STRING_SESSION - {str(e)}")
        sys.exit()


if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    try:
        if Config.TG_BOT_USERNAME is not None:
            LOGS.info("جاري تحميل تليثون ساقط 😅")
            # ForTheGreatrerGood of beautification
            bot.tgbot = TelegramClient(
                "TG_BOT_TOKEN", api_id=Config.APP_ID, api_hash=Config.API_HASH
            ).start(bot_token=Config.TG_BOT_TOKEN)
            LOGS.info("اكتمل تحميل وتنزيل تليثون ساقط بدون اخطاء 👍")
            LOGS.info("الان يتم بدء عمل بوت تليثون ساقط 🤖")
            bot.loop.run_until_complete(add_bot(Config.TG_BOT_USERNAME))
            LOGS.info("اكتمل التنصيب وتم بدء عمل بوت تليثون ساقط 👾")
        else:
            bot.start()
    except Exception as e:
        LOGS.error(f"TG_BOT_TOKEN - {str(e)}")
        sys.exit()

path = "userbot/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        try:
            if shortname.replace(".py", "") not in Config.NO_LOAD:
                load_module(shortname.replace(".py", ""))
            else:
                os.remove(Path(f"userbot/plugins/{shortname}.py"))
        except Exception as e:
            os.remove(Path(f"userbot/plugins/{shortname}.py"))
            LOGS.info(f"𖠕 لايمكن تنصيب ملف - {shortname} بسبب {e} 𖠕")

LOGS.info("بوت تليثون ساقط يعمل بنجاح 👽")
LOGS.info("لطلب المساعدة تعال الى هنا \n @OORRR 👍")


async def startupmessage():
    try:
        if Config.PRIVATE_GROUP_BOT_API_ID != 0:
            await bot.send_message(
                Config.PRIVATE_GROUP_BOT_API_ID,
                "𝆹𝅥𝅮 𝗍𝖾𝗅𝖾𝗍𝗁𝗈𝗇-𝖺𝗋𝖺𝖻𝗌 - 𝗎𝗉𝖽𝖺𝗍𝖾 𝗆𝗌𝗀 𝆹𝅥𝅮\n 𓍹ⵧⵧⵧⵧⵧⵧⵧⵧ𝐓𝐄𝐋𝐄𝐓𝐇𝐎𝐍 𝐒𝐀𝐐𝐓⁦⁦ⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n**⪼ مبروك عزيزي اكتب الان      .alive\n لترى ما اذا كان كات بوت يعمل**\
        \n ⪼ إذا كنت بحاجة إلى مساعدة راسل مطوري\n 𓍹ⵧⵧⵧⵧⵧⵧⵧⵧ𝐓𝐄𝐋𝐄𝐓𝐇𝐎𝐍 𝐒𝐀𝐐𝐓⁦⁦ⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n 𓆰 𝘚𝘖𝘜𝘙𝘊 𝘛𝘌𝘓𝘌𝘛𝘏𝘖𝘕  [DEV](t.me/OORRR)  𓆪",
                link_preview=False,
            )
    except Exception as e:
        LOGS.info(str(e))


bot.loop.create_task(startupmessage())

if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    bot.run_until_disconnected()
