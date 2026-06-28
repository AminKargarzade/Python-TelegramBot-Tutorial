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
    logger.info("Triggered welcome :)")
    markup = InlineKeyboardMarkup()
    button_google = InlineKeyboardButton("Google", url="https://www.google.com")
    button_my_github = InlineKeyboardButton("My_Github", url="https://github.com/AminKargarzade")
    button_test = InlineKeyboardButton("Test", callback_data="test")
    markup.add(button_google, button_my_github)
    markup.add(button_test)
    bot.send_message(
        message.chat.id,
        """Hi This is a sample for learning telegram bot in python.""",
        reply_markup=markup,
    )


@bot.callback_query_handler(func=lambda call: True)
def reply_call(call):
    # logger.info(call.__dict__)
    if call.data == "test":
        bot.answer_callback_query(
            call.id, "You clicked the test button!", show_alert=False
        )


bot.infinity_polling()
