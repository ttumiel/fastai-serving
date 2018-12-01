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
dispatcher = Dispatcher(bot, new_updates)#, None, workers=0)#
imgHandler = MessageHandler(Filters.photo, evaluate_image)
cmdHandler = CommandHandler(["start", "help"], help_message)
dispatcher.add_handler(imgHandler)
dispatcher.add_handler(cmdHandler)

# Start the thread
thread = Thread(target=dispatcher.start, name='dispatcher')
thread.start()

class Predict(View):
    def post(self, request, bot_token):
        global new_updates

        if bot_token != TOKEN:
            return HttpResponseForbidden('Invalid token')
        data = json.loads(request.body.decode('utf-8'))
        update = Update.de_json(data, bot)

        new_updates.put(update)

        # try:
        #     payload = json.loads(raw)
        # except ValueError:
        #     return HttpResponseBadRequest('Invalid request body')

        return JsonResponse({"Status": 1}, status=200)

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(Predict, self).dispatch(request, *args, **kwargs)