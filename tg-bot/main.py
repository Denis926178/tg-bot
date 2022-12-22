import telebot
from telebot import types
import random


# /// START GLOBAL VARIABLES ///


flag            = 0
bot             = telebot.TeleBot('5648594793:AAFEQ3l14VkaAPLYI-Ko8_oCZq8HajXSQvM')
base_dir_pic    = './congratulation_pic/'
base_dir_text   = './congratulation/'
expansion_pic   = '.gif'
expansion_text  = '.txt'

# /// END GLOBAL VARIABLES ///



# /// FUNCTION TO START BOT ///


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Выбрать праздник")
    markup.add(btn1)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Я тестовый бот для и я готов тебе отправить тебе то самое \
         поздравление, которое ты будешь всем прислылать в WhatsUp".format(message.from_user), reply_markup=markup)


# /// FUNCTION TO GET PICTURE AND TEXT AND SEND IT TO USER///


def get_data(message, dir, markup2):
    flag = 1
    string = "Вы можете вернуться в главное меню или попросить другое поздравление)"
    while flag:
        try:

            number  = random.randint(0, 50)
            pic     = base_dir_pic + dir + str(number) + expansion_pic
            f       = open(base_dir_text + dir + str(number) + expansion_text)
            text    = f.readline()
            flag    = 0

            f.close()
            bot.send_photo(message.chat.id, photo=open(pic, 'rb'), caption=text)
            button = types.KeyboardButton("Отправить другое поздравление")
            back = types.KeyboardButton("Вернуться в главное меню")
            markup2.add(button, back)

            bot.send_message(message.chat.id, text=string, reply_markup=markup2)
        except:
            ...



# /// FUNCTION THAT WHAIT MESSAGE FROM USER AND GOING WHAT HE WANTS


@bot.message_handler(content_types=['text'])
def func(message):
    markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)

    string = """Я могу отправить следующие поздравления:
    1) Новый год
    2) День Рождения
    3) Поздравить любимого
    4) 8 Марта"""

    if (message.text == "Выбрать праздник" or message.text == "Вернуться в главное меню"):
        button1 = types.KeyboardButton("8 Марта")
        button2 = types.KeyboardButton("День Рождения")
        button3 = types.KeyboardButton("Новый год")
        button4 = types.KeyboardButton("Поздравить любимого")
        markup1.row(button1, button2)
        markup1.row(button3, button4)
        bot.send_message(message.chat.id, text=string, reply_markup=markup1)

    elif (message.text == "8 Марта" or (message.text == "Отправить другое поздравление")):
        get_data(message, '8_march/', markup2)
    
    elif(message.text == "Новый год" or (message.text == "Отправить другое поздравление")):
        get_data(message, 'new_year/', markup2)
    
    elif (message.text == "День Рождения" or (message.text == "Отправить другое поздравление")):
        get_data(message, 'birthday/', markup2)

    elif (message.text == "Поздравить любимого" or (message.text == "Отправить другое поздравление")):
        get_data(message, 'love/', markup2)

    else:
        bot.send_message(message.chat.id, text="На такую комманду я не запрограммироваy...")

bot.polling(none_stop=True)