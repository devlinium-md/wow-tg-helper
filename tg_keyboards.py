import telebot

# Button library

run_wow = telebot.types.InlineKeyboardButton(text='Run WoW', callback_data='run_wow')
screenshot = telebot.types.InlineKeyboardButton(text="Take screenshot", callback_data='screenshot')
screenshot_menu = telebot.types.InlineKeyboardButton(text="Screenshot Menu", callback_data='screenshot_menu')
no_afk = telebot.types.InlineKeyboardButton(text="No AFK mode", callback_data='no_afk')
main_menu = telebot.types.InlineKeyboardButton(text="Main menu", callback_data='main_menu')
enter = telebot.types.InlineKeyboardButton(text="Press Enter", callback_data='enter')
start_no_afk = telebot.types.InlineKeyboardButton(text="Start", callback_data="start_no_afk")
stop_no_afk = telebot.types.InlineKeyboardButton(text="Stop", callback_data="stop_no_afk")
screenshot_on = telebot.types.InlineKeyboardButton(text="ENABLE auto", callback_data="screenshot_on")
screenshot_off = telebot.types.InlineKeyboardButton(text="DISABLE auto", callback_data="screenshot_off")



# Menu library

menu = telebot.types.InlineKeyboardMarkup()
menu.add(run_wow, screenshot_menu, no_afk)

screenshot_menu0 = telebot.types.InlineKeyboardMarkup()
screenshot_menu0.add(screenshot, screenshot_on, main_menu)

screenshot_menu1 = telebot.types.InlineKeyboardMarkup()
screenshot_menu1.add(screenshot, screenshot_off, main_menu)

no_afk_menu0 = telebot.types.InlineKeyboardMarkup()
no_afk_menu0.add(enter, start_no_afk, main_menu)

no_afk_menu1 = telebot.types.InlineKeyboardMarkup()
no_afk_menu1.add(enter, stop_no_afk, main_menu)
