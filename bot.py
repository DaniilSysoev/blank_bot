import telebot
from telebot import types
from listofnames import Names
from sendemail import send_email

Token = "5519023847:AAEAFMCXbeaQDdd1Sx5WWerJQw7WiLp5lYo"
bot = telebot.TeleBot(Token)


client = ""
name_coal = ""
weight_coal = ""
pay = ""
value_pay = ""
adress = ""
timing = ""
number = ""
text_comment = ""
blank = ""
flag = ""
new_client = ""

@bot.message_handler(commands=["start"])
def start(message):
    global flag
    flag = "start"
    global blank
    blank = """Клиент: {0}
Название угля: {1}
Количество угля: {2} кг
Способ оплаты: оплата {3}
Сумма оплаты: {4} р
Адрес: {5}
Время: {6}
Телефон: {7}
Комментарий: {8}""".format(client, name_coal, weight_coal, pay, value_pay, adress, timing, number,
                                       text_comment)
    if message.text == "/start" and message.from_user.username in Names.admins:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Заполнить заявку")
        btn3 = types.KeyboardButton("Посмотреть заявку")
        btn4 = types.KeyboardButton("Отправить заявку")
        markup.add(btn1, btn3, btn4)
        bot.send_message(message.chat.id, "Хотите заполнить заявку?", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, "Извините, я вас не узнаю")


def new_blank(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Показать клиентов")
    btn2 = types.KeyboardButton("Внести нового")
    btn3 = types.KeyboardButton("Отмена")
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id, "Показать клиентов или внести нового?", reply_markup=markup)


def show_clients(message):
    with open("clients.txt", "r", encoding="utf8") as file:
        clients = [i for i in file.readlines()]
        file.close()
    text = ["/client_{0}    {1}".format(str(i+1), clients[i]) for i in range(len(clients))]
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton("Название угля")
    btn2 = types.KeyboardButton("Отмена")
    markup.add(btn, btn2)
    bot.send_message(message.chat.id, "Выберите клиента:\n"+"\n".join(text), reply_markup=markup)


def get_client(message):
    global client
    with open("clients.txt", "r", encoding="utf8") as file:
        clients = [i for i in file.readlines()]
        file.close()
    client = clients[int(message.text[-1])-1]
    print(client)
    bot.send_message(message.chat.id, "Выбран клиент " + client)


def coal_name(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton("Количество угля")
    btn2 = types.KeyboardButton("Отмена")
    markup.add(btn, btn2)
    text = ["/name_{0}  {1}".format(str(i + 1), Names.name_of_coal[i]) for i in range(len(Names.name_of_coal))]
    bot.send_message(message.chat.id, "Выберите название угля:\n"+"\n".join(text), reply_markup=markup)


def get_coal_name(message):
    global name_coal
    name_coal = Names.name_of_coal[int(message.text[-1])-1]
    print(name_coal)
    bot.send_message(message.chat.id, "Выбран уголь " + name_coal)


def coal_weight(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton("Способ оплаты")
    btn2 = types.KeyboardButton("Отмена")
    markup.add(btn, btn2)
    bot.send_message(message.chat.id, "Введите количество угля", reply_markup=markup)


def get_coal_weight(message):
    global weight_coal
    weight_coal = message.text
    print(weight_coal)
    bot.send_message(message.chat.id, "Количество угля " + weight_coal)


def payment(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Наличная")
    btn2 = types.KeyboardButton("Безналичная")
    btn3 = types.KeyboardButton("Сумма оплаты")
    btn4 = types.KeyboardButton("Отмена")
    markup.add(btn1, btn2, btn3, btn4)
    bot.send_message(message.chat.id, "Выберите способ оплаты", reply_markup=markup)


def get_payment(message):
    global pay
    pay = message.text
    print(pay)
    bot.send_message(message.chat.id, "Оплата " + pay)


def value_payment(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton("Адрес")
    btn2 = types.KeyboardButton("Отмена")
    markup.add(btn, btn2)
    bot.send_message(message.chat.id, "Введите сумму оплаты", reply_markup=markup)


def get_value_payment(message):
    global value_pay
    value_pay = message.text
    print(value_pay)
    bot.send_message(message.chat.id, "Сумма оплаты " + value_pay)


def ask_adress(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton("Время")
    btn2 = types.KeyboardButton("Отмена")
    markup.add(btn, btn2)
    bot.send_message(message.chat.id, "Введите адрес", reply_markup=markup)


def get_adress(message):
    global adress
    adress = message.text
    print(adress)
    bot.send_message(message.chat.id, "Адрес " + adress)


def time(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton("Телефон")
    btn2 = types.KeyboardButton("Отмена")
    markup.add(btn, btn2)
    bot.send_message(message.chat.id, "Введите время", reply_markup=markup)


def get_time(message):
    global timing
    timing = message.text
    print(timing)
    bot.send_message(message.chat.id, "Время " + timing)


def telephone(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton("Комментарий")
    btn2 = types.KeyboardButton("Отмена")
    markup.add(btn, btn2)
    bot.send_message(message.chat.id, "Введите телефон", reply_markup=markup)


def get_telephone(message):
    global number
    number = message.text
    print(number)
    bot.send_message(message.chat.id, "Телефон " + number)


def comment(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton("Завершить")
    markup.add(btn)
    bot.send_message(message.chat.id, "Введите комментарий", reply_markup=markup)


def get_comment(message):
    global text_comment
    text_comment = message.text
    print(text_comment)
    bot.send_message(message.chat.id, "Комментарий: " + text_comment)


def show_blank(message):
    bot.send_message(message.chat.id, blank)


def send_blank(message):
    send_email([client, name_coal, weight_coal, pay, value_pay, adress, timing, number, text_comment])


def create_new_client(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Добавить")
    btn2 = types.KeyboardButton("Отмена")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, "Введите нового клиента", reply_markup=markup)


def get_new_client(message):
    global new_client
    new_client = message.text
    bot.send_message(message.chat.id, "Клиент: " + new_client)


def set_new_client(message):
    global flag
    global new_client
    flag = "Показать клиентов"
    with open("clients.txt", "a", encoding="utf8") as file:
        file.writelines("\n" + new_client)
        file.close()
    show_clients(message)

@bot.message_handler(content_types=["text"])
def func(message):
    global flag
    if message.text == "Заполнить заявку" and message.from_user.username in Names.admins:
        new_blank(message)
    elif (message.text == "Отмена" or message.text == "Завершить") and message.from_user.username in Names.admins:
        message.text = "/start"
        start(message)
        flag = "start"
    elif message.text == "Посмотреть заявку" and message.from_user.username in Names.admins:
        show_blank(message)
    elif message.text == "Внести нового" and message.from_user.username in Names.admins:
        create_new_client(message)
        flag = "Новый клиент"
    elif flag == "Новый клиент" and message.text != "Добавить" and message.from_user.username in Names.admins:
        get_new_client(message)
    elif flag == "Новый клиент" and message.text == "Добавить" and message.from_user.username in Names.admins:
        set_new_client(message)
    elif message.text == "Показать клиентов" and message.from_user.username in Names.admins:
        show_clients(message)
        flag = "Показать клиентов"
    elif flag == "Показать клиентов" and message.text[0] == "/" and message.text[1:7:] == "client" and message.from_user.username in Names.admins:
        get_client(message)
    elif message.text == "Название угля":
        coal_name(message)
        flag = "Название угля"
    elif message.text[0] == "/" and message.text[1:5:] == "name" and message.from_user.username in Names.admins:
        print(message.text)
        get_coal_name(message)
    elif message.text == "Количество угля" and message.from_user.username in Names.admins:
        coal_weight(message)
        flag = "Количество угля"
    elif message.text != "Способ оплаты" and flag == "Количество угля" and message.from_user.username in Names.admins:
        get_coal_weight(message)
    elif message.text == "Способ оплаты" and message.from_user.username in Names.admins:
        payment(message)
        flag = "Способ оплаты"
    elif (message.text == "Наличная" or message.text == "Безналичная") and message.from_user.username in Names.admins:
        get_payment(message)
    elif message.text == "Сумма оплаты" and message.from_user.username in Names.admins:
        value_payment(message)
        flag = "Сумма оплаты"
    elif message.text != "Адрес" and flag == "Сумма оплаты" and message.from_user.username in Names.admins:
        get_value_payment(message)
    elif message.text == "Адрес" and message.from_user.username in Names.admins:
        ask_adress(message)
        flag = "Адрес"
    elif flag == "Адрес" and message.text != "Время" and message.from_user.username in Names.admins:
        get_adress(message)
    elif message.text == "Время" and message.from_user.username in Names.admins:
        time(message)
        flag = "Время"
    elif message.text != "Телефон" and flag == "Время" and message.from_user.username in Names.admins:
        get_time(message)
    elif message.text == "Телефон" and message.from_user.username in Names.admins:
        telephone(message)
        flag = "Телефон"
    elif message.text != "Комментарий" and flag == "Телефон" and message.from_user.username in Names.admins:
        get_telephone(message)
    elif message.text == "Комментарий" and message.from_user.username in Names.admins:
        comment(message)
        flag = "Комментарий"
    elif flag == "Комментарий" and message.from_user.username in Names.admins:
        get_comment(message)
    elif message.text == "Посмотреть заявку" and message.from_user.username in Names.admins:
        show_blank(message)
    elif message.text == "Отправить заявку" and message.from_user.username in Names.admins:
        send_blank(message)
    else:
        if not(message.from_user.username in Names.admins):
            bot.send_message(message.chat.id, "Извините, я вас не узнаю")
    print(flag)


bot.polling(none_stop=True)