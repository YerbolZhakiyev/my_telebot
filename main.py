import telebot
from telebot import types

bot = telebot.TeleBot('5875110972:AAEPOJgUjDXJpX3IOxOFO0MlthWOg980UZg')

@bot.message_handler(commands=['start'])
def start(message): 
    mess = f'Добро пожаловать, <b>{message.from_user.first_name}</b>!'
    bot.send_message(message.chat.id, mess, parse_mode='html')
    bot.send_message(message.chat.id, "Для того чтобы посмотреть все комманды введите " + f"<b>/</b>", parse_mode='html')

@bot.message_handler(commands=['help'])
def help(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    make_order = types.KeyboardButton('Сделать заказ.')
    order_list = types.KeyboardButton('Посмотреть заказы.')
    markup.add(make_order, order_list)
    bot.send_message(message.chat.id, "Меню", reply_markup=markup)


@bot.message_handler(commands=['insta'])
def insta(msg):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Instagram:", url="https://www.instagram.com/zhakiev/"))
    bot.send_message(msg.chat.id, "Instagram", reply_markup=markup)

@bot.message_handler(commands=['telegram'])
def telegram(msg):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Telegram:", url="https://t.me/YerbolZ"))
    bot.send_message(msg.chat.id, "Telegram", reply_markup=markup)

# @bot.message_handler(content_types=['text'])
# def get_user_text(message):
#     if message.text == "Hello":
#         bot.send_message(message.chat.id, f"И тебе привет, {message.from_user.first_name}!")
#     elif message.text == "id":
#         bot.send_message(message.chat.id, f"Твой ID: {message.from_user.id}")
#     else:
#         bot.send_message(message.chat.id, "Неправильная команда.")

# @bot.message_handler(commands=['make_order'])
# def make_order(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
#     make_order = types.KeyboardButton('Сделать заказ.')
#     markup.add(make_order)
#     bot.send_message(message.chat.id, "Меню", reply_markup=markup)

bot.polling(non_stop=True)