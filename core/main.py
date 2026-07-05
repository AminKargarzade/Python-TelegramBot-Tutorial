import telebot
import os
import logging

logger = telebot.logger
telebot.logger.setLevel(logging.INFO)


API_TOKEN = os.environ.get("API_TOKEN", "")
bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=["pin"])
def pin_message_handler(message):
    bot.send_message(
        message.chat.id,
        "Give me the message you want to pin, and I will pin it for you!",
    )
    bot.register_next_step_handler(message, message_pinner)


def message_pinner(message):
    bot.pin_chat_message(message.chat.id, message.message_id)


bot.infinity_polling()
