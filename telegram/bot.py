from telegram.ext import MessageHandler, Filters, CommandHandler, Updater
from telegram.ext.dispatcher import run_async
from telegram import ParseMode
import logging, os

from .models.utils import pytorch
from config import BASE_FILE_PATH, TG_TOKEN

logging.basicConfig(format='[%(asctime)s][%(name)s][%(levelname)s] %(message)s',
	level=logging.INFO)

logger = logging.getLogger(__name__)

help_message = "" # Read markdown from file!

@run_async
def send_help(bot, update):
	logger.info("start or help command")
	bot.send_message(update.message.chat_id, help_message,
		parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True)

@run_async
def evaluate_image(bot, update):
	logger.info("Image received")
	PredictImage(update.message).predict()

class PredictImage():
	def __init__(self, message):
		self.message = message
		self.image = message.photo[-1]
		self.chat_id = message.chat_id
		self.message_id = message.message_id
		self.file_path = BASE_FILE_PATH.format(self.chat_id, self.message_id)

	def download(self):
		new_file = self.image.bot.get_file(self.image.file_id)
		new_file.download(self.file_path)

	def reply(self, message):
		self.message.reply_message(f"Your image contains a {message[0]} with probability {message[1]}",
		reply_to_message_id=self.message_id) # reply message??

	def predict(self):
		self.download()
		msg = pytorch(self.file_path)
		self.reply(msg)
		# Remove images after classification??

	# def remove(self):
	# 	try:
	# 		os.remove(self.file_path)
	# 	except:
    #         pass

updater = Updater(token=os.environ.get('TG_TOKEN') or TG_TOKEN or "")
dispatcher = updater.dispatcher

def main():
	imgHandler = MessageHandler(Filters.photo, evaluate_image)
	cmdHandler = CommandHandler(["start", "help"], send_help)
	dispatcher.add_handler(imgHandler, cmdHandler)

	updater.start_polling(clean=True)
	updater.idle()

if __name__ == '__main__':
    main()