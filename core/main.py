import telebot
import os
import logging

logger = telebot.logger
telebot.logger.setLevel(logging.INFO)

API_TOKEN = os.environ.get("API_TOKEN", "")
bot = telebot.TeleBot(API_TOKEN)

# MarkDown
# *bold text*
# _italic text_
# `inline code`
# [inline URL](https://github.com/AminKargarzade)
# [mention](tg://user?id=USER_ID)

# HTML
# <b>bold text</b>
# <i>italic text</i>
# <code>inline code</code>
# <a href="https://github.com/AminKargarzade">inline URL</a>
# <a href="tg://user?id=USER_ID">mention</a>


@bot.message_handler(commands=["markdown"])
def handle_messages(message):
    bot.send_message(message.chat.id, "*bold text*", parse_mode="Markdown")
    bot.send_message(message.chat.id, "_italic text_", parse_mode="Markdown")
    bot.send_message(message.chat.id, "`import requests`", parse_mode="Markdown")
    bot.send_message(
        message.chat.id,
        "[inline URL](https://github.com/AminKargarzade)",
        parse_mode="Markdown",
    )
    bot.send_message(
        message.chat.id,
        f"[mention](tg://user?id={message.from_user.id})",
        parse_mode="Markdown",
    )


@bot.message_handler(commands=["html"])
def handle_messages2(message):
    bot.send_message(message.chat.id, "<b>bold text</b>", parse_mode="HTML")
    bot.send_message(message.chat.id, "<i>italic text</i>", parse_mode="HTML")
    bot.send_message(message.chat.id, "<code>inline code</code>", parse_mode="HTML")
    bot.send_message(
        message.chat.id,
        '<a href="https://github.com/AminKargarzade">inline URL</a>',
        parse_mode="HTML",
    )
    bot.send_message(
        message.chat.id,
        f'<a href="tg://user?id={message.from_user.id}">mention</a>',
        parse_mode="HTML",
    )


bot.infinity_polling()