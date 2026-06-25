import telebot
import os
import pprint
import json


API_TOKEN = os.environ.get("API_TOKEN", "")

bot = telebot.TeleBot(API_TOKEN)

# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    # pprint.pprint(message.chat.__dict__,width=4)
#     bot.reply_to(message, """\
# Hi there, I am EchoBot.
# I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
# """)
    bot.send_message(message.chat.id,json.dumps(message.chat.__dict__, indent=4,ensure_ascii=False))


bot.infinity_polling()