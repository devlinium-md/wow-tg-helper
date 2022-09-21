import keyboards as kb
import texts
from credentials import bot



class ApplyForm:
    def __init__(self, name):
        self.name = None
        self.surname = None
        self.phone = None
        self.value = None
        self.photo = None
        self.id = id


apply_phase = 0


@bot.message_handler(commands=['start'])
def start_message(message):
    ApplyForm.id = message.chat.id
    bot.send_message(chat_id=message.chat.id, text='Main menu', reply_markup=kb.menu)


@bot.message_handler(content_types=['text'])
def input_text(message):
    global apply_phase
    if apply_phase == 1:
        ApplyForm.name = message.text
        print(ApplyForm.name)
        bot_message_id = message.message_id - 1
        bot.delete_message(message_id=bot_message_id, chat_id=message.chat.id)
        bot.send_message(chat_id=message.chat.id, text='Введите вашу фамилию так как она указана в паспорте',
                         reply_markup=kb.reset)
        apply_phase = 2

    elif apply_phase == 2:
        ApplyForm.surname = message.text
        print(ApplyForm.surname)
        bot_message_id = message.message_id - 1
        bot.delete_message(message_id=bot_message_id, chat_id=message.chat.id)
        bot.send_message(chat_id=message.chat.id, text='Введите ваш номер телефона',
                         reply_markup=kb.reset)
        apply_phase = 3

    elif apply_phase == 3:
        ApplyForm.phone = message.text
        print(ApplyForm.phone)
        bot_message_id = message.message_id - 1
        bot.delete_message(message_id=bot_message_id, chat_id=message.chat.id)
        bot.send_message(chat_id=message.chat.id, text='Введите сумму долга',
                         reply_markup=kb.reset)
        apply_phase = 4

    elif apply_phase == 4:
        ApplyForm.value = message.text
        print(ApplyForm.value)
        bot_message_id = message.message_id - 1
        bot.delete_message(message_id=bot_message_id, chat_id=message.chat.id)
        bot.send_message(chat_id=message.chat.id, text='У вас есть рассписка на этот долг?',
                         reply_markup=kb.apply_accept)
        apply_phase = 5


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    global apply_phase
    # Run WoW client from launcher
    if call.data == "run_wow":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=texts.run_wow)
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


@bot.message_handler(content_types=["photo"])
def apply(message):
    global apply_phase
    if apply_phase == 6:
        ApplyForm.photo = message.photo[-1].file_id
        ApplyForm.id = message.chat.id
        # db.apply_register(str(ApplyForm.name), str(ApplyForm.surname), int(ApplyForm.phone), int(ApplyForm.value), ApplyForm.photo, str(ApplyForm.id))
        bot.send_message(chat_id=message.chat.id, text='Ваша заявка была зарегистрированна по id',
                         reply_markup=kb.menu)
        apply_phase = 0
    else:
        bot.send_message(chat_id=message.chat.id, text='Я не понимаю что вы от меня хотите', reply_markup=kb.menu)


# Thread(target=bot.infinity_polling, args=(0,)).start()


# bot.enable_save_next_step_handlers(delay=2)
# bot.load_next_step_handlers()
# bot.polling(none_stop=True, interval=0)
bot.polling()


