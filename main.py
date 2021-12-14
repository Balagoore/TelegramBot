import random
import telebot
import config
from telebot import types
from random import choice

bot = telebot.TeleBot(config.TOKEN)
name = ''
age = 0
@bot.message_handler(commands=['start'])
def Bibiks(message):
    bibik = open("bibiks/11.webp", "rb")
    bot.send_sticker(message.chat.id, bibik)

    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButtonPollType('Мысли')
    btn2 = types.KeyboardButtonPollType('РРЛРЛ')
    markup.add(btn1, btn2)

    bot.send_message(message.chat.id, "Не ходи вокруг гроба... Но как зовут тебя? Не Алексндр...".format(message.from_user), parse_mode="html", reply_markup=markup)
gorit = [
    "Не правы те, кто спорит со мной"
    "Если рано просыпаешься - жди ооо-ооо-ооо"
    "Дом твой всегда далеко"
    "Идти до света просто, но не практично"
    "Не возможно сделать из человека слепца только на десять часов"
    "Будет так, как сказало утро"
    "Умирать не хочется"
    "Недоброе дело это..."
    "Не верь, что ты есть"
] #Список мой

@bot.message_handler(content_types=["text", 'photo'])
def Padal(message):
    if message.text == 'Мысли':
        bot.send_message(message.chat.id, random.choice(gorit))



@bot.message_handler(content_types=['text'])
def Kanevsky(message):
    if message.text == '/reg':
        bot.send_message(message.from_user.id, "Имя назови свое, или утонешь...") #здесь пер-ю name падал...
        bot.register_next_step_handler(message, get_name)
    else:
        bot.send_message(message.from_user.id, '/reg скажи! Уже точит...')

def get_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'Узнать хочу лета твои... Не будет сна иначе')
    bot.register_next_step_handler(message, get_age)

def get_age(message):
    global age
    while age == 0:
        try:
             age = int(message.text)
        except Exception:
            bot.send_message(message.from_user.id, 'Введи полные лета свои. Горел.')

    bot.send_message(message.from_user.id, 'И снова приветсвую тебя, '+name+' ')


#Зачем я убил коростеля?
bot.polling(none_stop=True)
