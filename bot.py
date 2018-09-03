import telebot
import config
from telebot import  types
import os
from flask import Flask, request

bot = telebot.TeleBot(config.token)

server = Flask(__name__)

@bot.message_handler(commands=['start'])

def otvet(message):
   user_markup = types.InlineKeyboardMarkup()
   b1 = types.InlineKeyboardButton(text='Четная',callback_data='chet')
   b2 = types.InlineKeyboardButton(text='Нечетная',callback_data='nech')
   user_markup.row(b1,b2)
   bot.send_message(message.from_user.id,"""Привет, котечки-котяяяятки❤️❤️❤️

Выбирайте нужную недельку😘""",reply_markup=user_markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data == 'chet':
            user_markup = types.InlineKeyboardMarkup()
            b3 = types.InlineKeyboardButton(text='Понедельник',callback_data='pn')
            b4 = types.InlineKeyboardButton(text='Вторник', callback_data='vt')
            b5 = types.InlineKeyboardButton(text='Среда', callback_data='sr')
            b6 = types.InlineKeyboardButton(text='Четверг', callback_data='cht')
            b7 = types.InlineKeyboardButton(text='Пятница', callback_data='pt')
            b8 = types.InlineKeyboardButton(text='Суббота', callback_data='sb')
            b9 = types.InlineKeyboardButton(text='Назад',callback_data='back')
            user_markup.row(b3,b4)
            user_markup.row(b5, b6)
            user_markup.row(b7, b8)
            user_markup.add(b9)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Выбери день)',reply_markup=user_markup)

        elif call.data == 'nech':
            user_markup = types.InlineKeyboardMarkup()
            b10 = types.InlineKeyboardButton(text='Назад',callback_data='back')
            user_markup.add(b10)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Пока нет расписания на нечетную,извини((',reply_markup=user_markup)
        elif call.data == 'back':
            user_markup = types.InlineKeyboardMarkup()
            b1 = types.InlineKeyboardButton(text='Четная', callback_data='chet')
            b2 = types.InlineKeyboardButton(text='Нечетная', callback_data='nech')
            user_markup.row(b1, b2)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Выбирайте нужную недельку😘', reply_markup=user_markup)




        elif call.data == 'pn':
            user_markup = types.InlineKeyboardMarkup()
            b11 = types.InlineKeyboardButton(text='Назад', callback_data='back1')
            user_markup.add(b11)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="""Понедельник, четная неделя:
            
11:30 - 13:05 - Транспортировка - *ЛЕКЦИЯ*. 312/9

13.35 - 15:10 - Геомеханика - *ЛЕКЦИЯ*. 306/1

15:20 - 16:55 - Геомеханика - *ПРАКТИКА*. 306/1""",reply_markup=user_markup,parse_mode="Markdown")

        elif call.data == 'vt':
            user_markup = types.InlineKeyboardMarkup()
            b12 = types.InlineKeyboardButton(text='Назад', callback_data='back1')
            user_markup.add(b12)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="""Вторник, четная неделя:
            
8:00 - 9:35 - Технология и безопасность взрывных работ - *ЛЕКЦИЯ*. 793/7

9:45 - 11:20 - Технология и безопасность взрывных работ - *ПРАКТИКА*. 793/7

11:30 - 13:05 - Горное право - *ЛЕКЦИЯ*. 209/10""",reply_markup=user_markup,parse_mode="Markdown")

        elif call.data == 'sr':
            user_markup = types.InlineKeyboardMarkup()
            b13 = types.InlineKeyboardButton(text='Назад', callback_data='back1')
            user_markup.add(b13)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="""Среда, четная неделя:
            
9:45 - 11:20 - БЖД - *ЛЕКЦИЯ*. 417/1

11:30 - 13:05 - ШТЕР - *ЛЕКЦИЯ*. 300/1

13:35 - 15:10 - ШТЕР - *ЛЕКЦИЯ*. 300/1""",reply_markup=user_markup,parse_mode="Markdown")

        elif call.data == 'cht':
            user_markup = types.InlineKeyboardMarkup()
            b14 = types.InlineKeyboardButton(text='Назад', callback_data='back1')
            user_markup.add(b14)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="""Четверг, четная неделя:
            
9:45 - 11:20 - Фазовые переходы - Самарин - *ЛЕКЦИЯ*. 310/1

11:30 - 13:05 - БЖД - *ЛАБА*. 83,85,87а/ 6 корпус

13:35 - 15:10 - БЖД - *ЛАБА*. 83,85,87а/ 6 корпус""",reply_markup=user_markup,parse_mode="Markdown")

        elif call.data == 'pt':
            user_markup = types.InlineKeyboardMarkup()
            b15 = types.InlineKeyboardButton(text='Назад', callback_data='back1')
            user_markup.add(b15)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Отдыхай😏',reply_markup=user_markup)

        elif call.data == 'sb':
            user_markup = types.InlineKeyboardMarkup()
            b16 = types.InlineKeyboardButton(text='Назад', callback_data='back1')
            user_markup.add(b16)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Отдыхай😏',reply_markup=user_markup)



        elif call.data == 'back1':
            user_markup = types.InlineKeyboardMarkup()
            b3 = types.InlineKeyboardButton(text='Понедельник',callback_data='pn')
            b4 = types.InlineKeyboardButton(text='Вторник', callback_data='vt')
            b5 = types.InlineKeyboardButton(text='Среда', callback_data='sr')
            b6 = types.InlineKeyboardButton(text='Четверг', callback_data='cht')
            b7 = types.InlineKeyboardButton(text='Пятница', callback_data='pt')
            b8 = types.InlineKeyboardButton(text='Суббота', callback_data='sb')
            b9 = types.InlineKeyboardButton(text='Назад',callback_data='back')
            user_markup.row(b3,b4)
            user_markup.row(b5, b6)
            user_markup.row(b7, b8)
            user_markup.add(b9)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Выбери день)',reply_markup=user_markup)
        else:
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Это невозможно')




@bot.message_handler(commands=['help'])

def wer(message):
    bot.send_message(message.from_user.id,"""Спокойно ☝🏻

Я все порешаю 🛢 🛢 🛢

Жми /start""")


@bot.message_handler(content_types=['text'])
def f(message):
    if message.text == '🛢':
       bot.send_message(message.from_user.id, """💵💵💵

Жми /start""")
    else:
        bot.send_message(message.from_user.id,'Не понимаю) Лучше жми /start')

@server.route('/' + config.token, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://vikastarosta5ntf9.herokuapp.com/' + config.token)
    return "!", 200


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))



