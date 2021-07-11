from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_sticker("CAACAgUAAx0CQ8QTWQACCD9gpSGtPso-JueMmC6tCptx2H6VjAACngEAAmpqaFeIQbV46r_aFh8E")
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
                        "🎭SᴛꞮᴄᴋᴇƦꜱ🎭", callback_data="help_back"
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
                        "💬SUPPORT CHAT💬", url="https://t.me/TITANX_CHAT"
                    )
                ],    
                [    
                    InlineKeyboardButton(
                        "Yes✔️", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No❌", callback_data="close"
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
        f"""<b>Hi {message.from_user.first_name}!
\n/play <song name> - play song you requested
/dplay <song name> - play song you requested via deezer
/splay <song name> - play song you requested via jio saavn
/playlist - Show now playing list
/current - Show now playing
/song <song name> - download songs you want quickly
/search <query> - search videos on youtube with details
/deezer <song name> - download songs you want quickly via deezer
/saavn <song name> - download songs you want quickly via saavn
/video <song name> - download videos you want quickly
\n*Admins only*
/player - open music player settings panel
/pause - pause song play
/resume - resume song play
/skip - play next song
/end - stop music play
/userbotjoin - invite assistant to your chat
/admincache - Refresh admin list
 </b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💬SUPPORT CHAT💬", url="https://t.me/TITANX_CHAT"
                    )
                ]
            ]
        )
    )    
