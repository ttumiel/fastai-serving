# A simple script to help you determine the json message structure of
# incoming messages from your bot

from webhook.config import TG_TOKEN
from telegram.ext import Updater, Filters, MessageHandler
import json
import ast

updater = Updater(token=TG_TOKEN)
dispatcher = updater.dispatcher

def start(bot, update):
    print(json.dumps(ast.literal_eval(str(update)), indent=4, sort_keys=True))
    print()

start_handler = MessageHandler(Filters.all, start)
dispatcher.add_handler(start_handler)

updater.start_polling()
