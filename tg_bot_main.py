import tg_keyboards as kb
import texts
import telebot
import win_run_events as run
import logging

logging.basicConfig(filename='app.log', filemode='w', format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

bot = telebot.TeleBot(str(open("api.key", "r").readline()))
afk_mode = scr_mode = 0


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(chat_id=message.chat.id, text='Main menu', reply_markup=kb.menu)


try:
    @bot.callback_query_handler(func=lambda call: True)
    def callback_worker(call):
        global afk_mode, scr_mode
        # Run WoW client from launcher
        match call.data:
            case "run_wow":
                bot.send_message(chat_id=call.message.chat.id, text='Trying to launch WoW, please wait')
                text_in_message = run.start_wow()
                bot.send_message(chat_id=call.message.chat.id, text=text_in_message)
                bot.send_message(chat_id=call.message.chat.id, text='Main Menu', reply_markup=kb.menu)
            case "screenshot_menu":
                if scr_mode == 0:
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          text="Screenshot Menu", reply_markup=kb.screenshot_menu0)
                else:
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          text="Screenshot Menu", reply_markup=kb.screenshot_menu1)
            case "screenshot_on":
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Пока ещё не работает. Не нажимай!!!", reply_markup=kb.main_menu)
                bot.send_message(chat_id=call.message.chat.id, text='Main menu', reply_markup=kb.menu)
                # text_in_message = run.start_afk()
                # scr_mode = 1
                # bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                #                       text=text_in_message)
                # bot.send_message(chat_id=call.message.chat.id, text="No AFK menu", reply_markup=kb.no_afk_menu1)
            case "screenshot_off":
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Пока ещё не работает. Не нажимай!!!", reply_markup=kb.main_menu)
                bot.send_message(chat_id=call.message.chat.id, text='Main menu', reply_markup=kb.menu)
                # bot.send_message(chat_id=call.message.chat.id,
                #                  text="No AFK mode will be disabled on next Jump attempt. "
                #                       "Please wait")
                # message = run.stop_afk()
                # scr_mode = 0
                # bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=message)
                # bot.send_message(chat_id=call.message.chat.id, text="No AFK menu", reply_markup=kb.no_afk_menu0)
            case "screenshot":
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text=texts.screenshot)
                bot.send_photo(chat_id=call.message.chat.id, photo=run.screenshot())
                if scr_mode == 0:
                    bot.send_message(chat_id=call.message.chat.id, text="Screenshot Menu",
                                     reply_markup=kb.screenshot_menu0)
                else:
                    bot.send_message(chat_id=call.message.chat.id, text="Screenshot Menu",
                                     reply_markup=kb.screenshot_menu1)
            case "no_afk":
                if afk_mode == 0:
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          text="No AFK menu", reply_markup=kb.no_afk_menu0)
                else:
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          text="No AFK menu", reply_markup=kb.no_afk_menu1)
            case "main_menu":
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Main Menu", reply_markup=kb.menu)
            case "start_no_afk":
                message = run.start_afk()
                afk_mode = 1
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=message)
                bot.send_message(chat_id=call.message.chat.id, text="No AFK menu", reply_markup=kb.no_afk_menu1)
            case "stop_no_afk":
                bot.send_message(chat_id=call.message.chat.id, text="No AFK mode will be disabled on next Jump "
                                                                    "attempt. Please wait")
                message = run.stop_afk()
                afk_mode = 0
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=message)
                bot.send_message(chat_id=call.message.chat.id, text="No AFK menu", reply_markup=kb.no_afk_menu0)
            case "enter":
                message = "Enter is pressed"
                run.enter()
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=message)
                bot.send_message(chat_id=call.message.chat.id, text="Main Menu", reply_markup=kb.menu)
except Exception:
    pass


try:
    bot.polling()
except Exception:
    bot.polling()
