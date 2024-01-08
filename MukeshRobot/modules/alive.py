import asyncio
from platform import python_version as pyver

from pyrogram import __version__ as pver
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from telegram import __version__ as lver
from telethon import __version__ as tver

from MukeshRobot import SUPPORT_CHAT, pbot,BOT_USERNAME, OWNER_ID

PHOTO = [
    "https://telegra.ph/file/3134ed3b57eb051b8c363.jpg",
    "https://telegra.ph/file/6ca0813b719b6ade1c250.jpg",
    "https://telegra.ph/file/5a2cbb9deb62ba4b122e4.jpg",
    "https://telegra.ph/file/cb09d52a9555883eb0f61.jpg",
    "https://telegra.ph/file/c5952790fa8235f499749.jpg",
]

Mukesh = [
    [
        InlineKeyboardButton(text="📍𝐎𝐰𝐧𝐞𝐫📍", url=f"tg://user?id={OWNER_ID}"),
        InlineKeyboardButton(text="🍒𝐆𝐫𝐨𝐮𝐩🍒", url=f"https://t.me/{SUPPORT_CHAT}"),
    ],
    [
        InlineKeyboardButton(
            text="☆ 𝐀𝐝𝐝 𝐌𝐞 𝐌𝐚𝐡𝐭𝐨 𝐀𝐧𝐣𝐚𝐥𝐢 ☆",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
]

lol = "https://te.legra.ph/file/471ef129b9c1b479676fd.jpg"


@pbot.on_message(filters.command("alive"))
async def restart(client, m: Message):
    await m.delete()
    accha = await m.reply("⚡")
    await asyncio.sleep(0.5)
    await accha.edit("ᴅɪɴɢ ᴅᴏɴɢ ꨄ︎ ᴀʟɪᴠɪɴɢ..")
    await asyncio.sleep(0.5)
    await accha.edit("ᴅɪɴɢ ᴅᴏɴɢ ꨄ︎ ᴀʟɪᴠɪɴɢ......")
    await asyncio.sleep(0.5)
    await accha.edit("ᴅɪɴɢ ᴅᴏɴɢ ꨄ︎ ᴀʟɪᴠɪɴɢ..")
    await asyncio.sleep(0.5)
    await accha.edit("ᴅɪɴɢ ᴅᴏɴɢ ꨄ︎ ᴀʟɪᴠɪɴɢ......")
    await accha.delete()
    await asyncio.sleep(0.5)
    umm = await m.reply_sticker(
        "CAACAgUAAxkDAAJHbmLuy2NEfrfh6lZSohacEGrVjd5wAAIOBAACl42QVKnra4sdzC_uKQQ"
    )
    await umm.delete()
    await asyncio.sleep(0.8)
    await m.reply_photo(
        lol,
        caption=f"""**🌷ʜᴇʏ, ɪ ᴀᴍ 『[𝗔𝗡𝗝𝗔𝗟𝗜 𝗥𝗢𝗕𝗢𝗧](f"t.me/{BOT_USERNAME}")』🎄**
   ╔═════ஜ۩۞۩ஜ════╗

   ♨️𝗠𝗔𝗗𝗘 𝗕𝗬 [𓆩 ᴍᴧʜᴛᴏ ✗ ᴧɴᴊᴀʟɪ 𓆪](https://t.me/QUEENx_GOD)♨️

   ╚═════ஜ۩۞۩ஜ════╝""",
        reply_markup=InlineKeyboardMarkup(Mukesh),
    )
__mod_name__ = "♨️ᴀʟɪᴠᴇ♨️"
__help__ = """

*ᴜsᴇʀ ᴄᴏᴍᴍᴀɴᴅs*:
» /alive*:* ᴛᴏ ᴄʜᴇᴀᴋ ❓  ɪ ᴀᴍ ᴀʟɪᴠᴇ ᴏʀ ɴᴏᴛ?

☆............𝙱𝚈 » [𓆩 ᴍᴧʜᴛᴏ ✗ ᴧɴᴊᴀʟɪ 𓆪](https://t.me/QUEENx_GOD)............☆"""
