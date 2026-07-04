import telebot
import os
import logging

logger = telebot.logger
telebot.logger.setLevel(logging.INFO)


API_TOKEN = os.environ.get("API_TOKEN", "")
bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(func=lambda message: message.chat.type in ["group", "supergroup"])
def handle_group_message(message):
    logger.info("Group Triggered!")


@bot.message_handler(func=lambda message: message.chat.type in ["private"])
def handle_private_message(message):
    logger.info("Private Triggered!")


bot.infinity_polling()
