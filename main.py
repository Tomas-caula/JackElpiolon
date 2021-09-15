import config
import telebot
import requests
import json 
import config 
import telebot


bot = config.API_KEY
DISCORD_SOLDADOS = config.DISCORD_WEBHOOKS
CHATID = "1826733848"

 
@bot.message_handler(commands=['Hi'])
def greet(message):
  bot.reply_to(message, "Hey! Hows it going?")


 
bot.polling()