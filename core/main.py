import telebot
import os
import logging

logger = telebot.logger
telebot.logger.setLevel(logging.INFO)


API_TOKEN = os.environ.get("API_TOKEN", "")
bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=["start"])
def send_welcome(message):
    logger.info(message.chat.__dict__)
    bot.send_message(
        message.chat.id, """Hi This is a sample for learning telegram bot in python."""
    )


@bot.message_handler(commands=["test_voice"])
def send_voice_file(message):
    voice_file = open("./test/files/test.mp3", "rb")
    bot.send_chat_action(message.chat.id, action="upload_voice")
    bot.send_voice(message.chat.id, voice_file)


@bot.message_handler(commands=["test_video"])
def send_video_file(message):
    bot.send_chat_action(message.chat.id, action="upload_video")
    bot.send_video(message.chat.id, open("./test/files/test.mp4", "rb"))


@bot.message_handler(commands=["test_document"])
def send_document_file(message):
    bot.send_chat_action(message.chat.id, action="upload_document")
    bot.send_document(message.chat.id, open("./test/files/test.pdf", "rb"))


@bot.message_handler(commands=["test_photo"])
def send_photo_file(message):
    bot.send_chat_action(message.chat.id, action="upload_photo")
    bot.send_document(message.chat.id, open("./test/files/test.jpg", "rb"))
    bot.send_photo(message.chat.id, open("./test/files/test.jpg", "rb"))


bot.infinity_polling()