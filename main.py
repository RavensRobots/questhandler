from telegram.ext import CommandHandler, Updater
import parser
from bot_token import TOKEN

updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="start message")


def new(update, context):
    command, items = parser.from_command_message_to_list(update.effective_message.text)
    for i in items:
        context.bot.send_message(chat_id=update.effective_chat.id, text=i)


start_handler = CommandHandler('start', start)
new_handler = CommandHandler('new', new)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(new_handler)
updater.start_polling()
