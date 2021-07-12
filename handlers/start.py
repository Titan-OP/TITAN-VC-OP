from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_sticker("")
    await message.reply_text(
        f"""<b>Hɪ {message.from_user.first_name}!
\nɪ ᴀᴍ [𝐓𝐈𝐓𝐀𝐍 𝐕𝐂 𝐁𝐎𝐓](https://telegra.ph/file/9221dea55a8e847788d92.jpg)
ɪ ᴄᴀɴ ᴘʟᴀʏ ᴍᴜꜱɪᴄ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ'ꜱ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ

🔹Mᴜꜱɪᴄ Aꜱꜱɪꜱᴛᴀɴᴛ🔹:- [Tɪᴛᴀɴ Vᴄ Aꜱꜱɪꜱᴛᴀɴᴛ](https://t.me/TITANVC_ASSISTANT)
\nᴛᴏ ᴀᴅᴅ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴄᴏɴᴛᴀᴄᴛ ᴜꜱ ᴀᴛ [Sᴜᴘᴘᴏʀᴛ Cʜᴀᴛ](https://t.me/TITANX_CHAT)
\nʜɪᴛ /help ᴛᴏ ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ᴀᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅꜱ.
 </b>""",
      
       
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                      "✨Tɪᴛᴀɴ Vᴄ Aꜱꜱɪꜱᴛᴀɴᴛ✨", url="https://t.me/TITANVC_ASSISTANT",
                    )
                ],
                [
                    InlineKeyboardButton(
                        "💬Sᴜᴘᴘᴏʀᴛ Cʜᴀᴛ💬", url="https://t.me/TITANX_CHAT"
                    ),
                    InlineKeyboardButton(
                        "🎭SᴛꞮᴄᴋᴇƦꜱ🎭", url="https://t.me/Stickersbag"
                    ),
                    InlineKeyboardButton(
                        "👑Oᴡɴᴇʀ👑", url="http://t.me/DARK_DEVIL_OP"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "💫 Aᴅᴅ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ 💫", url="https://t.me/VCSong21_bot?startgroup=true"
                    ) 
                ]
            ]
        )
    )

@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "💁🏻‍♂️ Do you want to search for a YouTube video?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💬Sᴜᴘᴘᴏʀᴛ Cʜᴀᴛ💬", url="https://t.me/TITANX_CHAT"
                    )
                ],    
                [    
                    InlineKeyboardButton(
                        "👑Cʀᴇᴀᴛᴏʀ👑", url="https://t.me/DARK_DEVIL_OP"
                    ),
                    InlineKeyboardButton(
                        "Nᴏ ❌", callback_data="close"
                    )
                ]
            ]
        )
    )

@Client.on_message(
    filters.command("help")
    & filters.private
    & ~ filters.edited
)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Hɪ {message.from_user.first_name}!
\n➟ Uꜱᴇʀ Cᴏᴍᴍᴀᴅꜱ
\n/play <song name> - play song you requested
\n/dplay <song name> - play song you requested via deezer
\n/splay <song name> - play song you requested via jio saavn
\n/playlist - Show now playing list
\n/current - Show now playing
\n/song <song name> - download songs you want quickly
\n/search <query> - search videos on youtube with details
\n/deezer <song name> - download songs you want quickly via deezer
\n/saavn <song name> - download songs you want quickly via saavn
\n/video <song name> - download videos you want quickly
\n\n➟ Aᴅᴍɪɴꜱ Cᴏᴍᴍᴀᴅꜱ
\n/player - open music player settings panel
\n/pause - pause song play
\n/resume - resume song play
\n/skip - play next song
\n/end - stop music play
\n/userbotjoin - invite assistant to your chat
\n/admincache - Refresh admin list
 </b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💬Sᴜᴘᴘᴏʀᴛ Cʜᴀᴛ💬", url="https://t.me/TITANX_CHAT"
                    )
                ]
            ]
        )
    )    
