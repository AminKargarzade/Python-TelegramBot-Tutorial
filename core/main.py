import telebot
import os
import logging
from telebot.types import ChatPermissions

logger = telebot.logger
telebot.logger.setLevel(logging.INFO)

API_TOKEN = os.environ.get("API_TOKEN", "")
bot = telebot.TeleBot(API_TOKEN)


def is_admin(message):
    chat_id = message.chat.id
    user_id = message.from_user.id

    user_info = bot.get_chat_member(chat_id, user_id)
    return user_info.status in ["administrator", "creator"]


@bot.message_handler(func=is_admin, commands=["restrict"])
def handle_restriction(message):
    permissions = ChatPermissions(
        can_send_messages=False,
        can_send_media_messages=False,
        can_send_audios=False,
        can_send_documents=False,
        can_send_photos=False,
        can_send_videos=False,
        can_send_video_notes=False,
        can_send_voice_notes=False,
        can_send_polls=False,
        can_send_other_messages=False,
        can_add_web_page_previews=False,
        can_react_to_messages=False,
    )
    bot.set_chat_permissions(message.chat.id, permissions=permissions)
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_message(
        message.chat.id,
        "Night Mode Activated! All members are restricted from sending messages,go sleep now!",
    )
    logger.info("Applying Restriction")


@bot.message_handler(func=is_admin, commands=["unrestrict"])
def handle_unrestriction(message):
    permissions = ChatPermissions(
        can_send_messages=True,
        can_send_media_messages=True,
        can_send_audios=True,
        can_send_documents=True,
        can_send_photos=True,
        can_send_videos=True,
        can_send_video_notes=True,
        can_send_voice_notes=True,
        can_send_polls=True,
        can_send_other_messages=True,
        can_add_web_page_previews=True,
        can_react_to_messages=True,
    )
    bot.set_chat_permissions(message.chat.id, permissions=permissions)
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_message(
        message.chat.id,
        "Day Mode Activated! All members are now allowed to send messages.Talk now!",
    )
    logger.info("Removing Restriction")


bot.infinity_polling()
