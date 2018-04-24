# Import bot token from environment variables
from os import environ
botToken = environ.get("MR_ROBOTO_TOKEN")

# Create updater and save reference to dispatcher
from telegram.ext import Updater
updater = Updater(token=botToken)
dispatcher = updater.dispatcher;

# Set up logging errors
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Function to run with the start command
def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="beep boop")

# Function to run with the new command
def new(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="new beep boop")

from telegram.ext import CommandHandler
# Add command handler for start command
start_handler = CommandHandler("start", start)
dispatcher.add_handler(start_handler)

# Add command handler for new command
new_handler = CommandHandler("new", new)
dispatcher.add_handler(new_handler)

# Start polling commands
updater.start_polling()
