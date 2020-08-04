from telegram.ext import CommandHandler, Updater
import re

updater = Updater(token="1142297593:AAGEcvmniWzAGmQVwpumaTtuIgaMoT7Yg9Y", use_context=True)
dispatcher = updater.dispatcher


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="start message")


def new(update, context):
    d = parse(update.effective_message.text)
    result = ""
    for v in d:
        result += "____ " + v
    context.bot.send_message(chat_id=update.effective_chat.id, text=result)


start_handler = CommandHandler('start', start)
new_handler = CommandHandler('new', new)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(new_handler)
updater.start_polling()


def parse(message):
    temp = re.match(r"/\w+ "
                    r"([\w ]+\.\.)?"
                    r"([\w ]+\.\.)?"
                    r"([\w ]+\.\.)?"
                    r"([\w ]+\.\.)?"
                    r"([\w ]+\.\.)?"
                    r"([\w ]+)", message)
    return temp.groups("")
