from config import TOKEN
from telebot import telebot, types 

bot = telebot.TeleBot(TOKEN)



@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('register/login')
    item2 = types.KeyboardButton('main page')
    markup.add(item1, item2)

    bot.reply_to(message, "Hey, how are you doing?", reply_markup=markup)


@bot.message_handler(commands=['help'])
def send_help(message):
	bot.reply_to(message, "What happened, bro?")


@bot.message_handler(content_types=['text'])
def go(message):
    if message.chat.type == 'private':
        if message.text == 'main page':
            bot.send_message(message.chat.id, 'http://127.0.0.1:8000/')
        elif message.text == 'register/login':
            bot.send_message(message.chat.id, 'http://127.0.0.1:8000/admin/')
        else:
            bot.reply_to(message, message.text)






bot.infinity_polling()