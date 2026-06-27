import telebot
import os
import logging
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

logger = telebot.logger
telebot.logger.setLevel(logging.INFO)


API_TOKEN = os.environ.get("API_TOKEN", "")
bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=["start"])
def send_welcome(message):
    logger.info("Triggered welcome :)")
    markup = ReplyKeyboardMarkup(
        resize_keyboard=True,
        input_field_placeholder="Choose Your option: ",
        one_time_keyboard=True,
    )
    markup.add(KeyboardButton("Help"), KeyboardButton("About"))
    bot.send_message(
        message.chat.id,
        """Hi This is a sample for learning telegram bot in python.""",
        reply_markup=markup,
    )


@bot.message_handler(func=lambda message: message.text == "Help")
def send_help(message):
    bot.send_message(message.chat.id, "This is the help message.")


@bot.message_handler(func=lambda message: message.text == "About")
def send_about(message):
    bot.send_message(message.chat.id, "This is the about message.")


bot.infinity_polling()