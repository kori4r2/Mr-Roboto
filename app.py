# Import bot token from environment variables
import inspect
import localDatabase as database
from os import environ
import botCommands as botCommands
botToken = environ.get("MR_ROBOTO_TOKEN")

# Create updater and save reference to dispatcher
from telegram.ext import Updater
updater = Updater(token=botToken)
dispatcher = updater.dispatcher;

# Set up logging errors
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Get list of commands available from the module
array = inspect.getmembers(botCommands, inspect.isfunction)
commList = [item[0] for item in array]

from telegram.ext import CommandHandler
for cmdString in commList:
    new_handler = CommandHandler(cmdString, getattr(botCommands, cmdString))
    dispatcher.add_handler(new_handler)

# Start polling commands
updater.start_polling()
