from django.shortcuts import render
from django.http import HttpResponseForbidden, HttpResponseBadRequest, JsonResponse
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.conf import settings

from queue import Queue
from threading import Thread
import os, json

from telegram import Bot, Update
from telegram.ext import Dispatcher, MessageHandler, Filters, CommandHandler, Updater

from .config import TG_TOKEN
from .bot import evaluate_image, help_message

TOKEN = os.environ.get('TG_TOKEN') or TG_TOKEN or ""

bot = Bot(TOKEN)
new_updates = Queue()
dispatcher = Dispatcher(bot, new_updates)
imgHandler = MessageHandler(Filters.photo, evaluate_image)
cmdHandler = CommandHandler(["start", "help"], help_message)
dispatcher.add_handler(imgHandler, cmdHandler)

# Start the thread
thread = Thread(target=dispatcher.start, name='dispatcher')
thread.start()

class Predict(View):
    def post(self, request, bot_token):
        if bot_token != TOKEN:
            return HttpResponseForbidden('Invalid token')

        update = Update.de_json(json.loads(request.body), bot)
        new_updates.put(update)

        # try:
        #     payload = json.loads(raw)
        # except ValueError:
        #     return HttpResponseBadRequest('Invalid request body')

        return JsonResponse({}, status=200)