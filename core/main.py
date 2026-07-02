import telebot
import os
import logging
from telebot.types import InlineQueryResultArticle, InputTextMessageContent

logger = telebot.logger
telebot.logger.setLevel(logging.INFO)


API_TOKEN = os.environ.get("API_TOKEN", "")
bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.send_message(
        message.chat.id, """Hi This is a sample for learning telegram bot in python."""
    )


@bot.inline_handler(func=lambda query: len(query.query) >= 0)
def query_handler(query):
    logger.info(query)
    results = []

    results.append(
        InlineQueryResultArticle(
            id="1",
            title="This is a test",
            input_message_content=InputTextMessageContent(
                message_text="This is a response"
            ),
            description="This is a description ",
        )
    )
    results.append(
        InlineQueryResultArticle(
            id="2",
            title="Join the bot",
            input_message_content=InputTextMessageContent(message_text="JOIN the bot"),
            url="https://t.me/py_rastin_bot",
        )
    )

    results.append(
        InlineQueryResultArticle(
            id="3",
            title="Check out my Github",
            input_message_content=InputTextMessageContent(
                message_text="https://github.com/AminKargarzade"
            ),
            url="https://github.com/AminKargarzade",
        )
    )

    bot.answer_inline_query(query.id, results, cache_time=0)


bot.infinity_polling()