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
    bot.send_message(
        message.chat.id, """Hi This is a sample for learning telegram bot in python."""
    )


@bot.message_handler(commands=["author"])
def send_author(message):
    markup = InlineKeyboardMarkup()
    myGithubButton = InlineKeyboardButton(
        "My Github", url="https://github.com/AminKargarzade"
    )
    markup.add(myGithubButton)
    bot.send_message(
        message.chat.id, "This bot was created by AminRastin !", reply_markup=markup
    )


bot.infinity_polling()