from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from ISTKHARX import app
from config import BOT_USERNAME
from ISTKHARX.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """
✰ 𝗪ᴇʟᴄᴏᴍᴇ ᴛᴏ 𝗧ᴇᴀᴍ 𝐈sᴛᴋʜᴀʀ 𝗥ᴇᴘᴏs ✰
 
✰ 𝗥ᴇᴘᴏ ᴛᴏ 𝗡ʜɪ 𝗠ɪʟᴇɢᴀ 𝗬ʜᴀ
 
✰ 𝗣ᴀʜʟᴇ 𝗣ᴀᴘᴀ 𝗕ᴏʟ 𝗥ᴇᴘᴏ 𝗢ᴡɴᴇʀ ᴋᴏ 

✰ || @ll_THUNDER_lll ||
 
✰ 𝗥ᴜɴ 24x7 𝗟ᴀɢ 𝗙ʀᴇᴇ 𝗪ɪᴛʜᴏᴜᴛ 𝗦ᴛᴏᴘ
 
"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("𝗔ᴅᴅ ᴍᴇ 𝗠ᴀʙʏ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("𝐑ᴇᴘᴏ", url="https://github.com/TEAM-ISTKHAR/MUSARRAT"),
          InlineKeyboardButton("⍣ ፝֠֩ ̶ ̶ꭘⷪ ͓ ꯭፝֠֩͠ ̶꯭ ̶͓𝚰𝛅꯭𝗍ᴋ꯭ʜᴧ꯭ꝛ", url="https://t.me/+czQ48LDbT1cxMWQ1"),
          ],
               [
                InlineKeyboardButton("𝗧ᴇᴀᴍ 𝗣ᴜʀᴠɪ 𝗕ᴏᴛs", url=f"https://t.me/PURVI_SUPPORT"),
],
[
InlineKeyboardButton("𝗠ᴀɪɴ 𝗕ᴏᴛ", url=f"https://t.me/PURVI_MUSIC_BOT"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://files.catbox.moe/60ay2d.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
