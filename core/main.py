import os
import uuid
import logging
import mimetypes

import requests
import telebot

# ==========================
# Configuration
# ==========================

API_TOKEN = os.environ.get("API_TOKEN", "")

DOWNLOAD_DIR = "downloads"
MAX_FILE_SIZE = 50 * 1024 * 1024  # 50 MB
REQUEST_TIMEOUT = 30

os.makedirs(DOWNLOAD_DIR, exist_ok=True)

logger = telebot.logger
logger.setLevel(logging.INFO)

bot = telebot.TeleBot(API_TOKEN)

# ==========================
# Commands
# ==========================

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(
        message.chat.id,
        "👋 Send me a direct file URL.\n\n"
        "Supported:\n"
        "🖼 Photos\n"
        "🎥 Videos\n"
        "🎵 Music\n"
        "📄 Documents\n"
        "📦 Any downloadable file"
    )


# ==========================
# Helpers
# ==========================

def get_filename(response, url):
    """
    Try to determine filename.
    """

    cd = response.headers.get("Content-Disposition")

    if cd and "filename=" in cd:
        filename = cd.split("filename=")[-1].replace('"', "").strip()

    else:
        filename = os.path.basename(url.split("?")[0])

    if not filename:
        extension = mimetypes.guess_extension(
            response.headers.get("Content-Type", "").split(";")[0]
        )

        filename = str(uuid.uuid4())

        if extension:
            filename += extension

    return filename


def download_file(url):

    response = requests.get(
        url,
        stream=True,
        timeout=REQUEST_TIMEOUT,
        allow_redirects=True,
    )

    response.raise_for_status()

    content_length = response.headers.get("Content-Length")

    if content_length:

        if int(content_length) > MAX_FILE_SIZE:
            raise Exception("File is larger than allowed size.")

    filename = get_filename(response, url)

    file_path = os.path.join(DOWNLOAD_DIR, filename)

    # جلوگیری از overwrite
    if os.path.exists(file_path):

        base, ext = os.path.splitext(filename)

        file_path = os.path.join(
            DOWNLOAD_DIR,
            f"{base}_{uuid.uuid4().hex[:6]}{ext}",
        )

    downloaded = 0

    with open(file_path, "wb") as f:

        for chunk in response.iter_content(chunk_size=8192):

            if chunk:

                downloaded += len(chunk)

                if downloaded > MAX_FILE_SIZE:

                    f.close()

                    os.remove(file_path)

                    raise Exception("File exceeded maximum size.")

                f.write(chunk)

    content_type = response.headers.get("Content-Type", "").split(";")[0]

    return file_path, content_type


def send_downloaded_file(chat_id, message_id, file_path, content_type):

    with open(file_path, "rb") as file:

        reply = telebot.types.ReplyParameters(message_id)

        if content_type.startswith("image/"):

            bot.send_photo(
                chat_id,
                photo=file,
                caption="✅ Download complete.",
                reply_parameters=reply,
            )

        elif content_type.startswith("video/"):

            bot.send_video(
                chat_id,
                video=file,
                caption="✅ Download complete.",
                reply_parameters=reply,
            )

        elif content_type.startswith("audio/"):

            bot.send_audio(
                chat_id,
                audio=file,
                caption="✅ Download complete.",
                reply_parameters=reply,
            )

        elif content_type == "image/gif":

            bot.send_animation(
                chat_id,
                animation=file,
                caption="✅ Download complete.",
                reply_parameters=reply,
            )

        else:

            bot.send_document(
                chat_id,
                document=file,
                caption="✅ Download complete.",
                reply_parameters=reply,
            )


# ==========================
# Main Handler
# ==========================

@bot.message_handler(func=lambda message: True)
def handle_url(message):

    url = message.text.strip()

    logger.info(url)

    waiting = bot.reply_to(
        message,
        "⏳ Downloading..."
    )

    try:

        file_path, content_type = download_file(url)

        send_downloaded_file(
            message.chat.id,
            message.id,
            file_path,
            content_type,
        )

        bot.delete_message(
            message.chat.id,
            waiting.message_id
        )

        os.remove(file_path)

    except requests.exceptions.MissingSchema:

        bot.edit_message_text(
            "❌ Invalid URL.",
            message.chat.id,
            waiting.message_id,
        )

    except requests.exceptions.InvalidURL:

        bot.edit_message_text(
            "❌ Invalid URL.",
            message.chat.id,
            waiting.message_id,
        )

    except requests.exceptions.Timeout:

        bot.edit_message_text(
            "⌛ Connection timed out.",
            message.chat.id,
            waiting.message_id,
        )

    except requests.exceptions.ConnectionError:

        bot.edit_message_text(
            "🌐 Could not connect to server.",
            message.chat.id,
            waiting.message_id,
        )

    except Exception as e:

        logger.error(e)

        bot.edit_message_text(
            f"❌ {e}",
            message.chat.id,
            waiting.message_id,
        )


# ==========================
# Run
# ==========================

logger.info("Bot Started.")

bot.infinity_polling(skip_pending=True)