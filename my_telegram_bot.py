import telebot
from telebot import types
from config import token

bot = telebot.TeleBot(token)

buttons = ['\U000025B6 Youtube',
           '\U0001F680 Student',
           '\U0001F4BB Github',
           '\U0001F601 Fun',
           '\U00002753 Help']


@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btns = []

    for i in range(len(buttons)):
        btns.append(types.KeyboardButton(text=buttons[i]))

    markup.add(btns[0], btns[1])
    markup.add(btns[2], btns[3])
    markup.add(btns[4])

    m = f'Hello, {message.from_user.first_name}. My name is Ilya. I am a software engineer in R&D department.' \
        f' My specialty is computer vision and robotics. This bot will help you get familiar with my portfolio.' \
        f' Type /help to see other commands.'
    bot.send_message(chat_id, m, parse_mode='html', reply_markup=markup)
    bot.delete_message(chat_id, message.id)


@bot.message_handler(commands=['youtube'])
def youtube(message):
    chat_id = message.chat.id

    links = [r'https://youtu.be/AkxwrQtRAdE', r'https://youtu.be/6MVLES0Psok',
             r'https://youtu.be/XVB-H-CpW-w', r'https://youtu.be/hhrW0mHCW4Q']

    for link in links:
        bot.send_message(chat_id, link, parse_mode='html')
    bot.delete_message(chat_id, message.id)


@bot.message_handler(commands=['student'])
def student(message):
    chat_id = message.chat.id

    links = [r'https://youtu.be/SAabt7LhAtI', r'https://youtu.be/3KvWVUPXigU',
             r'https://youtu.be/lwe3VlcBnsE', r'https://youtu.be/d7Sv36VX6h8',
             r'https://youtu.be/YZpBEIWxCs8']

    for link in links:
        bot.send_message(chat_id, link, parse_mode='html')
    bot.delete_message(chat_id, message.id)


@bot.message_handler(commands=['github'])
def github(message):
    chat_id = message.chat.id

    link = r'https://github.com/Cremator-2?tab=repositories'
    file = open('img/GitHub-Logo.png', 'rb')
    bot.send_photo(chat_id, file)

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    url = types.InlineKeyboardButton('Link to GitHub', url=link)

    keyboard.add(url)

    bot.send_message(chat_id, link, reply_markup=keyboard)
    bot.delete_message(chat_id, message.id)


@bot.message_handler(commands=['fun'])
def fun(message):
    chat_id = message.chat.id

    m = r'https://youtu.be/5p1lI7Xt7lE'
    bot.send_message(chat_id, m, parse_mode='html')
    bot.delete_message(chat_id, message.id)


@bot.message_handler(commands=['help'])
def help_command(message):
    chat_id = message.chat.id

    m = '/start - to start again.\n' \
        '/youtube - to get links to videos of my works on youtube.\n' \
        '/student - to get links to videos of my student works on youtube.\n' \
        '/fun - tic-tac-toe.. just click).\n' \
        '/github - link to my github.'

    keyboard = types.InlineKeyboardMarkup()

    btns = []

    for i in range(len(buttons) - 1):
        btns.append(types.InlineKeyboardButton(buttons[i], callback_data=buttons[i]))

    keyboard.add(btns[0], btns[1])
    keyboard.add(btns[2], btns[3])

    bot.send_message(chat_id, m, parse_mode='html', reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def handle_text(message):
    buttons_to_func(message, message.text.strip())


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    buttons_to_func(call.message, call.data.strip())


def buttons_to_func(message, text):
    if text == buttons[0]:
        youtube(message)
    elif text == buttons[1]:
        student(message)
    elif text == buttons[2]:
        github(message)
    elif text == buttons[3]:
        fun(message)
    elif text == buttons[4]:
        help_command(message)
    else:
        text = 'Are you sure?'
        bot.reply_to(message, text)
        help_command(message)


if __name__ == "__main__":
    bot.polling(none_stop=True)
