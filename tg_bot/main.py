import telebot
from telebot import types
import psycopg2
import time
#-------------------Connect to db
conn = psycopg2.connect(dbname='tg_bot',
                        user='erbol', 
                        password='password',
                        host='db',
                        port='5432')
cursor = conn.cursor()

bot = telebot.TeleBot('5875110972:AAEPOJgUjDXJpX3IOxOFO0MlthWOg980UZg')        

@bot.message_handler(commands=['start'])
def start(message): 
    mess = f'Добро пожаловать, <b>{message.from_user.first_name}</b>!'
    bot.send_message(message.chat.id, mess, parse_mode='html')
    bot.send_message(message.chat.id, "Для того, чтобы посмотреть все комманды введите " + f"<b>/</b>", parse_mode='html')
    bot.send_message(message.chat.id, "Для того, чтобы сделать заказ введите " + f"<b>/create_order</b>", parse_mode='html')
    bot.send_message(message.chat.id, "Для того, чтобы сделать заказ введите " + f"<b>/all_orders</b>", parse_mode='html')
    bot.send_message(message.chat.id, "Спасибо, что используете этого бота.", parse_mode='html')
    name_of_customer = str(message.from_user.first_name)
    id_of_customer = message.from_user.id
#-------------------Check for new customer and adding him if does not exist
    sql_query_to_check_primary_key = "SELECT * FROM customers WHERE tg_id = %s"
    cursor.execute(sql_query_to_check_primary_key, (id_of_customer,))
    result = cursor.fetchone()
    if result is None:
#-------------------------------------
        cursor.execute("INSERT INTO customers (name, tg_id) VALUES (%s, %s)", (name_of_customer, id_of_customer))
        conn.commit()
#-------------------------------------
@bot.message_handler(commands=['insta'])
def insta(msg):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Instagram:", url="https://www.instagram.com/zhakiev/"))
    bot.send_message(msg.chat.id, "Instagram", reply_markup=markup)
#-------------------------------------
@bot.message_handler(commands=['telegram'])
def telegram(msg):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Telegram:", url="https://t.me/YerbolZ"))
    bot.send_message(msg.chat.id, "Telegram", reply_markup=markup)
#-------------------------------------
def get_order_id():
    return int(time.time())
@bot.message_handler(commands=['create_order'])
def create_order(message):
    id = get_order_id()
    cursor.execute("INSERT INTO orders (id) VALUES (%s)", (id,))
    conn.commit()
    bot.send_message(message.chat.id, 'Введите описание заказа. Опишите, что хотите отправить и количество товара (Например: Мешки сахара, 6 мешков; Коробки, 4 штуки; Телевизор и т.д.):')
    bot.register_next_step_handler(message, get_description, id)
def get_description(message, id):
    cursor.execute("UPDATE orders SET description = %s WHERE id = %s", (message.text, id))
    conn.commit()
    bot.send_message(message.chat.id, 'Введите вес заказа (Например: 120 киллограммов; 40 литров и т.д.):')
    bot.register_next_step_handler(message, get_weight, id)
def get_weight(message, id):
    cursor.execute("UPDATE orders SET weight = %s WHERE id = %s", (message.text, id))
    conn.commit()
    bot.send_message(message.chat.id, 'Введите адрес откуда необходимо забрать заказ:')
    bot.register_next_step_handler(message, get_from, id)
def get_from(message, id):
    cursor.execute("UPDATE orders SET from_address = %s WHERE id = %s", (message.text, id))
    conn.commit()
    bot.send_message(message.chat.id, 'Введите адрес куда необходимо доставить заказ:')
    bot.register_next_step_handler(message, get_where, id)
def get_where(message, id):
    cursor.execute("UPDATE orders SET to_address = %s WHERE id = %s", (message.text, id))
    conn.commit()
    bot.send_message(message.chat.id, 'Введите Номер телефона:')
    bot.register_next_step_handler(message, get_phone, id)
def get_phone(message, id):
    id_for_text = str(id)
    cursor.execute("UPDATE orders SET phone = %s WHERE id = %s", (message.text, id))
    conn.commit()         
    with open('/root/my_telebot/image2.jpeg', 'rb') as photo:
        bot.send_photo(message.chat.id, photo) 
    bot.send_message(message.chat.id, 'Заказ успешно создан! Номер вашего заказа: ' + id_for_text + ' Спасибо!')
#-------------------------------------
row_num = 0
@bot.message_handler(commands=['all_orders'])
def send_orders(message):
    cursor.execute("SELECT * FROM orders")
    rows = cursor.fetchall()
    num_rows = len(rows)
    chat_id = message.chat.id
    bot.send_message(chat_id, format_order_row(rows[row_num]))
    markup = telebot.types.ReplyKeyboardMarkup(row_width=2)
    previous_button = telebot.types.KeyboardButton('Предыдущий заказ')
    next_button = telebot.types.KeyboardButton('Следующий заказ')
    markup.add(previous_button, next_button)
    bot.send_message(chat_id, "Выберите действие:", reply_markup=markup)
    
    @bot.message_handler(func=lambda message: message.text == 'Предыдущий заказ')
    def handle_previous_order(message):
        global row_num
        row_num -= 1
        if row_num < 0:
            row_num = num_rows - 1
        bot.send_message(chat_id, format_order_row(rows[row_num]), reply_markup=markup)
        return handle_previous_order
    
    @bot.message_handler(func=lambda message: message.text == 'Следующий заказ')
    def handle_next_order(message):
        global row_num
        row_num += 1
        if row_num >= num_rows:
            row_num = 0
        bot.send_message(chat_id, format_order_row(rows[row_num]), reply_markup=markup)
        return handle_next_order
def format_order_row(row):
    return f"ID заказа: {row[0]}\nОписание: {row[1]}\nОткуда: {row[2]}\nКуда: {row[3]}\nВес: {row[4]}\nТелефон: {row[5]}"
#-------------------------------------

bot.polling(non_stop=True)        
