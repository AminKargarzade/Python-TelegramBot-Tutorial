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
    button_my_github = InlineKeyboardButton(
        "My_Github", url="https://github.com/AminKargarzade"
    )
    button_step1 = InlineKeyboardButton("Step 1", callback_data="step1")
    markup.add(button_google, button_my_github)
    markup.add(button_step1)
    bot.send_message(
        message.chat.id,
        """Hi This is a sample for learning telegram bot in python.""",
        reply_markup=markup,
    )


@bot.callback_query_handler(func=lambda call: True)
def reply_call(call):
    # logger.info(call.__dict__)
    if call.data == "step1":
        # bot.answer_callback_query(
        #     call.id, "You clicked the test button!", show_alert=False
        # )
        markup = InlineKeyboardMarkup()
        button_step2 = InlineKeyboardButton("Step 2", callback_data="step2")
        button_cancel = InlineKeyboardButton("Cancel", callback_data="cancel")
        markup.add(button_step2, button_cancel)
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.id,
            text="Choose Your Next Step: ",
            reply_markup=markup,
        )
    if call.data == "step2":
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.id,
            text="Your Refrence code is: 1234567890",
        )
    if call.data == "cancel":
        bot.answer_callback_query(
            call.id, "Process has been canceled!", show_alert=True
        )
        bot.delete_message(
            chat_id=call.message.chat.id, message_id=call.message.id, timeout=5
        )


bot.infinity_polling()
