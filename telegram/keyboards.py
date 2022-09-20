import telebot

# Button library

active_requests = telebot.types.InlineKeyboardButton(text='Active requests', callback_data='active')
historical_requests = telebot.types.InlineKeyboardButton(text='Historical requests', callback_data='history')
main_menu = telebot.types.InlineKeyboardButton(text='Main menu', callback_data='menu')
accept = telebot.types.InlineKeyboardButton(text='Accept', callback_data='accept')
cancel = telebot.types.InlineKeyboardButton(text='Cancel', callback_data='cancel')
done = telebot.types.InlineKeyboardButton(text='Done', callback_data='done')
unaccept = telebot.types.InlineKeyboardButton(text='Unaccept', callback_data='unaccept')


menu = telebot.types.InlineKeyboardMarkup()
menu.add(active_requests, historical_requests, main_menu)

request_ph1 = telebot.types.InlineKeyboardMarkup()
request_ph1.add(accept, cancel)

request_ph2 = telebot.types.InlineKeyboardMarkup()
request_ph2.add(done, unaccept, cancel)