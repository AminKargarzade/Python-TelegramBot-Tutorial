import telebot
import os
import logging

logger = telebot.logger
telebot.logger.setLevel(logging.INFO)

API_TOKEN = os.environ.get("API_TOKEN", "")
bot = telebot.TeleBot(API_TOKEN)

CHANNEL_ID = os.environ.get("CHANNEL_ID", "")


@bot.message_handler(commands=["start"])
def message_handler(message):
    logger.info(message.text.split()[1])


bot.infinity_polling()
