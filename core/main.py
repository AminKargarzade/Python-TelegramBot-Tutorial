import telebot
import os
import logging

logger = telebot.logger
telebot.logger.setLevel(logging.INFO)

API_TOKEN = os.environ.get("API_TOKEN", "")
bot = telebot.TeleBot(API_TOKEN)

CHANNEL_ID = os.environ.get("CHANNEL_ID", "")

bot.send_message(chat_id=CHANNEL_ID, text="Hello from the bot!")

# bot.infinity_polling() We don't need this anymore while interacting with Channels, because we're only sending messages and not listening for incoming messages!
