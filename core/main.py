import telebot
import os
import logging
import requests

logger = telebot.logger
telebot.logger.setLevel(logging.INFO)

if not os.path.exists("downloads"):
    os.makedirs("downloads")

API_TOKEN = os.environ.get("API_TOKEN", "")
bot = telebot.TeleBot(API_TOKEN)

DOWNLOAD_DIR = "downloads/"


@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.send_message(
        message.chat.id,
        "Give me a valid URL for a file and I will download it for you.",
    )


def download_file(url):
    local_filename = url.split("/")[-1]
    file_path = DOWNLOAD_DIR + local_filename
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(file_path, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return file_path


@bot.message_handler(func=lambda message: True)
def download_file_url(message):
    logger.info(message.text)
    url = message.text
    try:
        file_path = download_file(url)
        bot.send_document(chat_id=message.chat.id, reply_parameters=telebot.types.ReplyParameters(message.id), document=open(file_path, "rb"), caption="File downloaded successfully.")  # type: ignore
        # os.remove(file_path)  # Clean up the downloaded file after sending
    except requests.exceptions.RequestException as e:
        logger.error(f"Error occurred while downloading file from {url}: {e}")
        bot.reply_to(
            message,
            text="Failed to download the file. Please check the URL and try again.",
        )


bot.infinity_polling()
