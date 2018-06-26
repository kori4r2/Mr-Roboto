import localDatabase as database
# Function to run with the start command
def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="beep boop")

# Function to run with the new command
def new(bot, update):
#    bot.send_message(chat_id=update.message.chat_id, text=("new sent by" + update.effective_user.to_json()))
    userID = update.effective_user.id
    member = update.effective_chat.get_member(user_id=userID)
    bot.send_message(chat_id=update.message.chat_id, text="@"+member.user.username)
