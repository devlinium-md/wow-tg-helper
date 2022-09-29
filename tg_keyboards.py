import telebot

# Button library

run_wow_menu_call = telebot.types.InlineKeyboardButton(text='Run WoW Menu', callback_data='run_wow_menu_call')
run_wow_simple = telebot.types.InlineKeyboardButton(text='Simple Run', callback_data='run_wow_simple')
run_wow_auto = telebot.types.InlineKeyboardButton(text="Automated Run", callback_data='run_wow_auto')
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
menu.add(run_wow_menu_call, screenshot_menu, no_afk)

run_wow_menu = telebot.types.InlineKeyboardMarkup()
run_wow_menu.add(run_wow_simple, run_wow_auto, main_menu)

screenshot_menu0 = telebot.types.InlineKeyboardMarkup()
screenshot_menu0.add(screenshot, screenshot_on, main_menu)

screenshot_menu1 = telebot.types.InlineKeyboardMarkup()
screenshot_menu1.add(screenshot, screenshot_off, main_menu)

no_afk_menu0 = telebot.types.InlineKeyboardMarkup()
no_afk_menu0.add(enter, start_no_afk, main_menu)

no_afk_menu1 = telebot.types.InlineKeyboardMarkup()
no_afk_menu1.add(enter, stop_no_afk, main_menu)
