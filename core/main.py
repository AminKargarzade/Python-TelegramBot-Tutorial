import telebot
import os
import logging

logger = telebot.logger
telebot.logger.setLevel(logging.INFO)

API_TOKEN = os.environ.get("API_TOKEN", "")
bot = telebot.TeleBot(API_TOKEN)

# get_chat_administrators
# get_chat_member
# get_chat_members_count
# get_chat

# @bot.message_handler(func=lambda message: True)
# def handle_messages(message):
#     data = bot.get_chat(message.chat.id)
#     logger.info(data)

# @bot.message_handler(func=lambda message: True)
# def handle_messages(message):
#     data = bot.get_chat_member_count(message.chat.id)
#     logger.info(data)

# @bot.message_handler(func=lambda message: True)
# def handle_messages(message):
#     data = bot.get_chat_member(message.chat.id, message.from_user.id)
#     logger.info(data)

# @bot.message_handler(func=lambda message: True)
# def handle_messages(message):
#     data = bot.get_chat_administrators(message.chat.id)
#     for user in data:
#         logger.info(user)


@bot.message_handler(commands=["ban"])
def handle_messages(message):
    logger.info(message.text.split(" ")[1])


bot.infinity_polling()
