import telebot
import os
import logging

logger = telebot.logger
telebot.logger.setLevel(logging.INFO)

API_TOKEN = os.environ.get("API_TOKEN", "")
bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=["help", "start"])
def send_welcome(message):
    logger.info("Triggered welcome :)")
    bot.reply_to(
        message, """Hi This is a sample for learning telegram bot in python."""
    )


@bot.message_handler(commands=["setname"])
def setup_name(message):
    bot.send_message(message.chat.id, "What Is Your First Name?")
    bot.register_next_step_handler(message, assign_first_name)


def assign_first_name(message, *args, **kwargs):
    first_name = message.text
    bot.send_message(message.chat.id, "What Is Your Last Name?")
    bot.register_next_step_handler(message, assign_last_name, first_name)


def assign_last_name(message, first_name):
    last_name = message.text
    bot.send_message(message.chat.id, f"Welcome to my bot {first_name} {last_name}!")


bot.infinity_polling()
