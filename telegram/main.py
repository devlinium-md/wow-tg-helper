import operations as op
import keyboards as kb
import db_operations as db
from credentials import bot


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(chat_id=message.chat.id, text='Your ID is - ' + str(message.chat.id))


@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/queue':
        op.all_requests()


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    request_id = op.find_id(call.message.text)
    if call.data == "accept":
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=kb.request_ph2)
    elif call.data == "done":
        db.done(request_id)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='NICE')
    elif call.data == "unaccept":
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=kb.request_ph1)
    elif call.data == "cancel":
        db.delete(request_id)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Request canceled')


bot.polling(none_stop=True, interval=0)
