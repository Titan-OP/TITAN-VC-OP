from asyncio.queues import QueueEmpty
from cache.admins import set
from pyrogram import Client
from pyrogram.types import Message
from callsmusic import callsmusic
import traceback
import os
import sys
from pyrogram.errors.exceptions.bad_request_400 import ChatAdminRequired
from pyrogram.errors.exceptions.flood_420 import FloodWait
from pyrogram import filters, emoji
from config import BOT_NAME as BN
from helpers.filters import command, other_filters
from helpers.decorators import errors, authorized_users_only
from config import que, admins as a

@Client.on_message(filters.command('adminreset'))
async def update_admin(client, message):
    global a
    admins = await client.get_chat_members(message.chat.id, filter="administrators")
    new_ads = []
    for u in admins:
        new_ads.append(u.user.id)
    a[message.chat.id] = new_ads
    await message.reply_text('Sᴜᴄᴇꜱꜱꜰᴜʟʟʏ Uᴘᴅᴀᴛᴇᴅ Aᴅᴍɪɴ Lɪꜱᴛ Iɴ **{}**'.format(message.chat.title))




@Client.on_message(command("pause") & other_filters)
@errors
@authorized_users_only
async def pause(_, message: Message):
    if (
            message.chat.id not in callsmusic.pytgcalls.active_calls
    ) or (
            callsmusic.pytgcalls.active_calls[message.chat.id] == 'paused'
    ):
        await message.reply_text("❗ Nᴏᴛʜɪɴɢ Iꜱ Pʟᴀʏɪɴɢ!")
    else:
        callsmusic.pytgcalls.pause_stream(message.chat.id)
        await message.reply_text("**Lɪᴠᴇ Sᴛʀᴇᴀᴍ ɪꜱ Nᴏᴡ**\n➖➖➖➖➖➖➖\n▶️ **Pᴀᴜꜱᴇᴅ!**")


@Client.on_message(command("resume") & other_filters)
@errors
@authorized_users_only
async def resume(_, message: Message):
    if (
            message.chat.id not in callsmusic.pytgcalls.active_calls
    ) or (
            callsmusic.pytgcalls.active_calls[message.chat.id] == 'playing'
    ):
        await message.reply_text("❗ Nᴏᴛʜɪɴɢ Iꜱ Pᴀᴜꜱᴇᴅ!")
    else:
        callsmusic.pytgcalls.resume_stream(message.chat.id)
        await message.reply_text("**Lɪᴠᴇ Sᴛʀᴇᴀᴍ ɪꜱ Nᴏᴡ**\n➖➖➖➖➖➖➖\n⏸ **Rᴇꜱᴜᴍᴇᴅ!**")


@Client.on_message(command("end") & other_filters)
@errors
@authorized_users_only
async def stop(_, message: Message):
    if message.chat.id not in callsmusic.pytgcalls.active_calls:
        await message.reply_text("❗ Nᴏᴛʜɪɴɢ Iꜱ Sᴛʀᴇᴀᴍɪɴɢ!")
    else:
        try:
            callsmusic.queues.clear(message.chat.id)
        except QueueEmpty:
            pass

        callsmusic.pytgcalls.leave_group_call(message.chat.id)
        await message.reply_text("❌ Sᴛᴏᴘᴘᴇᴅ Sᴛʀᴇᴀᴍɪɴɢ!")


@Client.on_message(command("skip") & other_filters)
@errors
@authorized_users_only
async def skip(_, message: Message):
    global que
    if message.chat.id not in callsmusic.pytgcalls.active_calls:
        await message.reply_text("❗ Sᴏᴛʜɪɴɢ ɪꜱ Pʟᴀʏɪɴɢ ᴛᴏ Sᴋɪᴘ!")
    else:
        callsmusic.queues.task_done(message.chat.id)

        if callsmusic.queues.is_empty(message.chat.id):
            callsmusic.pytgcalls.leave_group_call(message.chat.id)
        else:
            callsmusic.pytgcalls.change_stream(
                message.chat.id,
                callsmusic.queues.get(message.chat.id)["file"]
            )
                

    qeue = que.get(message.chat.id)
    if qeue:
        skip = qeue.pop(0)
    if not qeue:
        return
    await message.reply_text(f'- Sᴋɪᴘᴘᴇᴅ **{skip[0]}**\n➖➖➖➖➖➖➖➖\n- Nᴏᴡ Pʟᴀʏɪɴɢ **{qeue[0][0]}**')


@Client.on_message(
    filters.command("admincache")
)
@errors
async def admincache(client, message: Message):
    set(message.chat.id, [member.user for member in await message.chat.get_members(filter="administrators")])
    #await message.reply_text("✯Tɪᴛᴀɴ Mᴜꜱɪᴄ✯ :\nAᴅᴍɪɴ Cᴀᴄʜᴇ Rᴇꜰʀᴇꜱʜᴇᴅ!💫")
