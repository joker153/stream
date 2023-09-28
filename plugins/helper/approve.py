import os
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message, User, ChatJoinRequest
from info import CHAT_ID, TEXT, APPROVED, WELCOME_TEXT, JOIN_CHANNEL_TEXT, JOIN_CHANNEL_LINK, AUTH_CHANNEL,


@Client.on_chat_join_request(filters.group | filters.channel)
async def custom_autoapprove(client: Client, message: ChatJoinRequest):
    chat = message.chat
    user = message.from_user
    print(f"{user.first_name} Joined 🤝")  # Logs

    # Define the specific channel's chat_id to exclude
    excluded_channel_chat_id = AUTH_CHANNEL

    if chat.id != excluded_channel_chat_id:
        await client.approve_chat_join_request(chat_id=chat.id, user_id=user.id)
        if APPROVED == "on":
            welcome_text = WELCOME_TEXT.format(mention=user.mention, title=chat.title)
            button = None
            if JOIN_CHANNEL_LINK:
                button = InlineKeyboardMarkup([[InlineKeyboardButton(JOIN_CHANNEL_TEXT, url=JOIN_CHANNEL_LINK)]])
            await client.send_message(chat_id=user.id, text=welcome_text, reply_markup=button)
