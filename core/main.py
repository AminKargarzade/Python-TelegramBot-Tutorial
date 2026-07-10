import telebot
import os
import logging

logger = telebot.logger
telebot.logger.setLevel(logging.INFO)

API_TOKEN = os.environ.get("API_TOKEN", "")
bot = telebot.TeleBot(API_TOKEN)

CHANNEL_ID = os.environ.get("CHANNEL_ID", "")
CHANNEL_LINK = "https://t.me/pyrastinchannel"


def is_member(message):
    user_info = bot.get_chat_member(CHANNEL_ID, message.from_user.id)
    if user_info.status not in ["member", "administrator", "creator"]:
        bot.send_message(
            message.chat.id,
            f"Please Subscribe to the channel first: [Join Channel]({CHANNEL_LINK}) ",
            parse_mode="Markdown",
        )
        return False
    return True


@bot.message_handler(func=is_member)
def message_handler(message):
    bot.reply_to(message, "ok")


bot.infinity_polling()
