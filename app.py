from os import environ
botToken = environ.get("MR_ROBOTO_TOKEN")

from telegram.ext import Updater
updater = Updater(token=botToken)

dispatcher = updater.dispatcher;

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="beep boop")

from telegram.ext import CommandHandler
start_handler = CommandHandler("start", start)
dispatcher.add_handler(start_handler)

updater.start_polling()
