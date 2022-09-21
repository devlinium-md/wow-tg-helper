import telebot

# Button library

run_wow = telebot.types.InlineKeyboardButton(text='Run WoW', callback_data='run_wow')
screenshot = telebot.types.InlineKeyboardButton(text="Take screenshot", callback_data='screenshot')
no_afk = telebot.types.InlineKeyboardButton(text="No AFK mode", callback_data='no_afk')
main_menu = telebot.types.InlineKeyboardButton(text="Вернуться к главному меню", callback_data='main_menu')
back = telebot.types.InlineKeyboardButton(text="Назад", callback_data='back')
apply_yes = telebot.types.InlineKeyboardButton(text="Да", callback_data='apply_yes')
apply_no = telebot.types.InlineKeyboardButton(text="Нет", callback_data='apply_no')


# Menu library

menu = telebot.types.InlineKeyboardMarkup()
menu.add(run_wow, screenshot, no_afk)

no_afk_menu = telebot.types.InlineKeyboardMarkup()
no_afk_menu.add(back, main_menu)

apply_accept = telebot.types.InlineKeyboardMarkup()
apply_accept.add(apply_yes, apply_no, back, main_menu)