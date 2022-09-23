import telebot

# Button library

run_wow = telebot.types.InlineKeyboardButton(text='Run WoW', callback_data='run_wow')
screenshot = telebot.types.InlineKeyboardButton(text="Take screenshot", callback_data='screenshot')
no_afk = telebot.types.InlineKeyboardButton(text="No AFK mode", callback_data='no_afk')
main_menu = telebot.types.InlineKeyboardButton(text="Main menu", callback_data='main_menu')
enter = telebot.types.InlineKeyboardButton(text="Press Enter", callback_data='enter')
start_no_afk = telebot.types.InlineKeyboardButton(text="Start", callback_data="start_no_afk")
stop_no_afk = telebot.types.InlineKeyboardButton(text="Stop", callback_data="stop_no_afk")



# Menu library

menu = telebot.types.InlineKeyboardMarkup()
menu.add(run_wow, screenshot, no_afk)

no_afk_menu1 = telebot.types.InlineKeyboardMarkup()
no_afk_menu1.add(enter, start_no_afk, main_menu)

no_afk_menu2 = telebot.types.InlineKeyboardMarkup()
no_afk_menu2.add(enter, stop_no_afk, main_menu)
