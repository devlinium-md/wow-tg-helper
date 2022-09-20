import telebot

# Button library

contact = telebot.types.InlineKeyboardButton(text='Контактная информация', callback_data='contact')
pay = telebot.types.InlineKeyboardButton(text="Хочу оплатить долг", callback_data='pay')
apply = telebot.types.InlineKeyboardButton(text="Заявочка", callback_data='apply')
main_menu = telebot.types.InlineKeyboardButton(text="Вернуться к главному меню", callback_data='main_menu')
back = telebot.types.InlineKeyboardButton(text="Назад", callback_data='back')
apply_yes = telebot.types.InlineKeyboardButton(text="Да", callback_data='apply_yes')
apply_no = telebot.types.InlineKeyboardButton(text="Нет", callback_data='apply_no')


# Menu library

menu = telebot.types.InlineKeyboardMarkup()
menu.add(contact, pay, apply)

reset = telebot.types.InlineKeyboardMarkup()
reset.add(back, main_menu)

apply_accept = telebot.types.InlineKeyboardMarkup()
apply_accept.add(apply_yes, apply_no, back, main_menu)