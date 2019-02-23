# Configuration for the telegram API

import os, sys

BASE_FILE_PATH = os.path.abspath(os.path.dirname(sys.argv[0])) + '/tmp/{}_{}.jpg' # check this is the same tmp
TG_TOKEN = TOKEN = os.environ.get('TG_TOKEN', '') # Telegram bot token
