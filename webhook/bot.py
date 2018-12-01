from telegram.ext.dispatcher import run_async
from telegram import ParseMode
from django.template.loader import render_to_string
import logging, os

import datamodels as D
from .config import BASE_FILE_PATH, TG_TOKEN

logging.basicConfig(format='[%(asctime)s][%(name)s][%(levelname)s] %(message)s',
	level=logging.INFO)

logger = logging.getLogger(__name__)

def _display_help():
    return render_to_string('telegram/help.md')

@run_async
def help_message(bot, update):
	logger.info(f"Command received: {update.message.text}")
	bot.send_message(update.message.chat_id, _display_help(),
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
		self.message.reply_text(message, reply_to_message_id=self.message_id)

	def predict(self):
		self.download()
		pred, prob = D.predict(self.file_path)
		self.reply(f"Your image contains a {pred} with probability {str(prob)}")
		# Remove images after classification??
		# self.remove()

	# def remove(self):
	# 	try:
	# 		os.remove(self.file_path)
	# 	except:
    #         pass
