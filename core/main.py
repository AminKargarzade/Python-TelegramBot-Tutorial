import telebot
import os
import logging

logger = telebot.logger
telebot.logger.setLevel(logging.INFO)  # Outputs debug messages to console.

API_TOKEN = os.environ.get("API_TOKEN", "")
bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=["help", "start"])
def send_welcome(message):
    logger.info("Triggered welcome :)")
    bot.reply_to(
        message, """Hi This is a sample for learning telegram bot in python."""
    )


bot.infinity_polling()
