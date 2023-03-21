import telebot
from telebot import types
import time
from dotenv import load_dotenv, find_dotenv
import os
import requests
import json
#-------------------------------------
dotenv_path = find_dotenv()
load_dotenv(dotenv_path)
TOKEN = os.getenv('TGTOKEN')
BACKEND_HOST = os.getenv('backend_host')

bot = telebot.TeleBot(TOKEN)   

#-------------------------------------
@bot.message_handler(commands=['start'])
def start(message): 
    mess = f'Добро пожаловать, <b>{message.from_user.first_name}</b>!'
    bot.send_message(message.chat.id, mess, parse_mode='html')
    bot.send_message(message.chat.id, "Для того, чтобы посмотреть все комманды введите: " + f"<b>/</b>", parse_mode='html')
    bot.send_message(message.chat.id, "Для того, чтобы сделать заказ введите " + f"<b>/create_order</b>", parse_mode='html')
    bot.send_message(message.chat.id, "Для того, чтобы посмотреть все заказы " + f"<b>/all_orders</b>", parse_mode='html')
    bot.send_message(message.chat.id, "Спасибо, что используете этого бота.", parse_mode='html')
    name_of_customer = str(message.from_user.first_name)
    id_of_customer = message.from_user.id
    json_data = json.dumps({'name': name_of_customer, 'tg_id': id_of_customer})
    headers = {'Content-Type': 'application/json', 'Accept': 'text/plain'}
    response = requests.post('http://backend:8000/api/customers', data=json_data, headers=headers)
#-------------------------------------
@bot.message_handler(commands=['web'])
def insta(msg):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Веб-Сайт:", url=BACKEND_HOST))
    bot.send_message(msg.chat.id, "Здесь вы можете посмотреть все заказы на сайте", reply_markup=markup)
#-------------------------------------
def get_order_id():
    return int(time.time())
@bot.message_handler(commands=['create_order'])
def create_order(message):
    id = get_order_id()
    bot.send_message(message.chat.id, 'Введите описание заказа. Опишите, что хотите отправить, желательно добавить все детали:')
    bot.register_next_step_handler(message, get_description, id)

def get_description(message, id):
    order = {"id": id, "description": message.text}
    markup = telebot.types.ReplyKeyboardMarkup(row_width=1)
    kg = telebot.types.KeyboardButton('Килограмм')
    t = telebot.types.KeyboardButton('Тонны')
    li = telebot.types.KeyboardButton('Литры')
    num = telebot.types.KeyboardButton('Шт.')
    markup.add(kg, t, li, num)
    bot.send_message(message.chat.id, 'Выберите единицы измерения:', reply_markup=markup)
    bot.register_next_step_handler(message, get_units, order, id)

def get_units(message, order, id):
    order["units"] = message.text
    bot.send_message(message.chat.id, 'Введите вес заказа:')
    bot.register_next_step_handler(message, get_weight, order, id)

def get_weight(message, order, id):
    order["weight"] = message.text
    bot.send_message(message.chat.id, 'Введите адрес откуда необходимо забрать заказ:')
    bot.register_next_step_handler(message, get_from, order, id)

def get_from(message, order, id):
    order["from_address"] = message.text
    bot.send_message(message.chat.id, 'Введите адрес куда необходимо доставить заказ:')
    bot.register_next_step_handler(message, get_where, order, id)

def get_where(message, order, id):
    order["to_address"] = message.text
    bot.send_message(message.chat.id, 'Введите Номер телефона:')
    bot.register_next_step_handler(message, get_phone, order, id)

def get_phone(message, order, id):
    order["phone"] = message.text
    response = requests.post("http://backend:8000/api/orders", json=order)      
    with open('/tg_bot/image2.jpeg', 'rb') as photo:
        bot.send_photo(message.chat.id, photo) 
    bot.send_message(message.chat.id, f'Заказ успешно создан! Номер вашего заказа: {id} Спасибо!')
#-------------------------------------

dict_num = 0
@bot.message_handler(commands=['all_orders'])
def send_orders(message):
    chat_id = message.chat.id
    response = requests.get('http://backend:8000/api/orders')
    json_obj = response.json()
    orders_array = json_obj['data']
    num_dicts = len(orders_array)
    
    def send_order_message(chat_id, dicti):
        markup = telebot.types.ReplyKeyboardMarkup(row_width=2)
        previous_button = telebot.types.KeyboardButton('Предыдущий заказ')
        next_button = telebot.types.KeyboardButton('Следующий заказ')
        markup.add(previous_button, next_button)
        bot.send_message(chat_id, f"ID заказа: {dicti['id']}\nОписание: {dicti['description']}\nОткуда: {dicti['from_address']}\nКуда: {dicti['to_address']}\nВес: {dicti['weight']}\nТелефон: {dicti['phone']}", reply_markup=markup)

    dicti = orders_array[dict_num]
    send_order_message(chat_id, dicti)
    
    @bot.message_handler(func=lambda message: message.text == 'Предыдущий заказ')
    def handle_previous_order(message):
        global dict_num
        dict_num -= 1
        if dict_num < 0:
            dict_num = num_dicts - 1
        dicti = orders_array[dict_num]
        send_order_message(chat_id, dicti)
    
    @bot.message_handler(func=lambda message: message.text == 'Следующий заказ')
    def handle_next_order(message):
        global dict_num
        dict_num += 1
        if dict_num >= num_dicts:
            dict_num = 0
        dicti = orders_array[dict_num]
        send_order_message(chat_id, dicti)
#-------------------------------------

bot.polling(non_stop=True)        