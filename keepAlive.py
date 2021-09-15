from flask import Flask
from threading import Thread
import config
import telebot
import requests
import json 
import config 


API_KEY_TELEGRAM = config.API_KEY
DISCORD_SOLDADOS = config.DISCORD_WEBHOOKS
app = Flask('')


@app.route('/')
def home():
    return "I'm alive"


def run():
    app.run(host='0.0.0.0', port=8080)


def keep_alive():
    t = Thread(target=run)
    t.start()


CHATID = "1826733848"
API_KEY = config.API_KEY
bot = telebot.TeleBot(API_KEY_TELEGRAM)

def Send_message_to_telegram (bot_message): 
  sendMessage = "https://core.telegram.org/bots/api" + API_KEY + "/sendMessage?chat_id" + CHATID + "&parse_mode=MarkdownV2&text=" + bot_message

  response = requests.get(sendMessage)
  return response.json()
