import tg_keyboards as kb
import texts
import telebot
import win_run_events as run

bot = telebot.TeleBot(str(open("api.key", "r").readline()))


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(chat_id=message.chat.id, text='Main menu', reply_markup=kb.menu)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    # Run WoW client from launcher
    if call.data == "run_wow":
        message = run.start_wow()
        # bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=texts.run_wow)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=message)
        bot.send_message(chat_id=call.message.chat.id, text='Main Menu', reply_markup=kb.menu)
    elif call.data == "screenshot":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=texts.screenshot)
        bot.send_photo(chat_id=call.message.chat.id, photo=open("/images/launcher.png", "rb"))
        bot.send_message(chat_id=call.message.chat.id, text='Главное Меню', reply_markup=kb.menu)
    elif call.data == "no_afk":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="No AFK menu", reply_markup=kb.no_afk_menu)
    elif call.data == "main_menu":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Главное меню",
                              reply_markup=kb.menu)


bot.polling()
