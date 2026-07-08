import telebot
import os
import logging

logger = telebot.logger
telebot.logger.setLevel(logging.INFO)

API_TOKEN = os.environ.get("API_TOKEN", "")
bot = telebot.TeleBot(API_TOKEN)

bad_words_list = [
    "badword1",
    "badword2",
    "badword3",
]  # Replace with your list of bad words


warnings = {}


def has_bad_words(text):
    return any(bad_word in text for bad_word in bad_words_list)


@bot.message_handler(func=lambda message: True)
def message_handler(message):

    if has_bad_words(message.text):
        if str(message.from_user.id) in warnings:
            warnings[str(message.from_user.id)] += 1
        else:
            warnings[str(message.from_user.id)] = 1

        if warnings[str(message.from_user.id)] > 3:
            bot.kick_chat_member(message.chat.id, message.from_user.id)
            bot.send_message(
                message.chat.id,
                f"{message.from_user.first_name} has been kicked out for using bad words.",
            )
        else:
            bot.reply_to(
                message,
                f"Don't use bad words! This is your {warnings[str(message.from_user.id)]} warnings, after 3rd warning you will be kicked out.",
            )


bot.infinity_polling()
