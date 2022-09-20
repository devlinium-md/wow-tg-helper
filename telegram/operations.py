import keyboards as kb
import db_operations as db
from credentials import bot

users = db.users()


def send_to_all(request):
    for user in users:
        text = \
            "ID - " + str(request[0]) + '  !\n' \
            "Date - " + str(request[5])[:16] + '\n' + \
            "Customer name - " + str(request[1]) + '\n' + \
            "Phone - " + (request[2]) + '\n' + \
            "Mail - " + str(request[3]) + '\n' + \
            "Commentary - " + str(request[4]) + '\n' + \
            "Work type - " + str(request[6]) + '\n'
        bot.send_message(chat_id=user, text=text, parse_mode='Markdown', reply_markup=kb.request_ph1)


def all_requests():
    tasks = db.active()
    for task in tasks:
        send_to_all(task)


def find_id(message):
    request_id = str(message)
    s = find_index(request_id, '!')
    request_id = request_id[:s]
    request_id = request_id.strip()
    request_id = int(request_id[5:])
    return request_id


def find_index(input_str, search_str):
    i = input_str.find(search_str, 0)
    return i
