import telebot
import config


bot = telebot.TeleBot(config.TOKEN)
name = ''
age = 0
@bot.message_handler(commands=['start'])
def Bibiks(message):
    bibik = open("bibiks/11.webp", "rb")
    bot.send_sticker(message.chat.id, bibik)

    bot.send_message(message.chat.id, "Не ходи вокруг гроба... Но как зовут тебя? Не Алексндр...".format(message.from_user), parse_mode="html")

#Зачем я убил коростеля?
bot.polling(none_stop=True)
