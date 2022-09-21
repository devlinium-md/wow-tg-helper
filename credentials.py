import telebot

key = open("api.key", "r")
key = str(key.readline())

bot = telebot.TeleBot(key)
