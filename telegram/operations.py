import keyboards as kb
from credentials import bot


def check(chat):
    bot.send_message(text="Введите ваше имя и фамили так как они указаны в паспорте", chat_id=chat)

    def send_welcome(message):
        msg = bot.reply_to(message, """\
    Hi there, I am Example bot.
    What's your name?
    """)
        bot.register_next_step_handler(msg, process_name_step)

    def process_name_step(message):
        try:
            chat_id = message.chat.id
            name = message.text
            user = User(name)
            user_dict[chat_id] = user
            msg = bot.reply_to(message, 'How old are you?')
            bot.register_next_step_handler(msg, process_age_step)
        except Exception as e:
            bot.reply_to(message, 'oooops')
