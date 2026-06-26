import telebot
import os

API_TOKEN = os.environ.get("API_TOKEN", "")

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=["help", "start"])
def send_welcome(message):
    bot.reply_to(
        message, """Hi This is a sample for learning telegram bot in python."""
    )


@bot.edited_message_handler(func=lambda message: True)
def edited_message(message):
    print("Triggered for edited message")


bot.infinity_polling()
