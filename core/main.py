import telebot
from telebot import apihelper
import os

apihelper.ENABLE_MIDDLEWARE = True

API_TOKEN = os.environ.get("API_TOKEN", "")

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=["help", "start"])
def send_welcome(message):
    bot.reply_to(
        message, """Hi This is a sample for learning telegram bot in python."""
    )


@bot.middleware_handler(update_types=["message"])
def modify_message(bot_instance, message):
    # modifying the message before it reaches any other handler
    message.another_text = message.text + ":changed :)"


@bot.message_handler(func=lambda message: True)
def reply_modified(message):
    bot.reply_to(message, message.another_text)


bot.infinity_polling()
