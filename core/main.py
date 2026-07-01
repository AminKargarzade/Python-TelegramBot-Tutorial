import telebot
import os
import logging
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

logger = telebot.logger
telebot.logger.setLevel(logging.INFO)


API_TOKEN = os.environ.get("API_TOKEN", "")
bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=["start"])
def send_welcome(message):
    logger.info(message.chat.__dict__)
    bot.send_message(
        message.chat.id, """Hi This is a sample for learning telegram bot in python."""
    )


@bot.message_handler(commands=["upload_test"])
def send_document_file(message):
    markup = InlineKeyboardMarkup()
    like_btn = InlineKeyboardButton("Like", callback_data="like")
    dislike_btn = InlineKeyboardButton("Dislike", callback_data="dislike")
    markup.add(like_btn, dislike_btn)
    bot.send_video(
        message.chat.id,
        "BAACAgQAAxkBAAIBMmpFDnKCyt4hykEgA1aCTgfDsXZzAAKCHwACR3MpUgZnsUqOtLtpPAQ",
        caption="This is a sample video file",
        reply_markup=markup,
    )


@bot.message_handler(
    content_types=["document", "video_note", "video", "audio", "voice", "photo"]
)
def check_id(message):
    logger.info(message.__dict__)


bot.infinity_polling()