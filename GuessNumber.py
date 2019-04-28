import telebot
from telebot import types
import random

#подключаемся к боту
bot = telebot.TeleBot("write_here_your_token")
num=0

#эта функция ловит только команды
@bot.message_handler(commands=['start'])
def handle_command(msg):
    chat_id=msg.chat.id
    name=msg.chat.first_name
    
    reply="Hello," + name + "!"

    keyboard = types.InlineKeyboardMarkup()#создаем клавиатуру
    btn = types.InlineKeyboardButton("Let's play!", callback_data="play")
    keyboard.add(btn)
    
    bot.send_message(chat_id,reply, reply_markup=keyboard)

#эта функция ловит нажатие кнопок
@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    global num   
    chat_id = call.message.chat.id
    num = random.randint(1,10)
    reply="Guess the number from 1 to 10!"
    bot.send_message(chat_id,reply)

#эта функция ловит обычный текст
@bot.message_handler(content_types=["text"])
def handle_text(msg):
    global num
    chat_id=msg.chat.id
    mynum = int(msg.text)
    if mynum>num:
        bot.send_message(chat_id,"Less...")
    elif mynum<num:
        bot.send_message(chat_id,"Bigger...")
    else:
        keyboard = types.InlineKeyboardMarkup()#создаем клавиатуру
        btn = types.InlineKeyboardButton("Let's play again!", callback_data="play")
        keyboard.add(btn)
        bot.send_message(chat_id,"You got it!", reply_markup=keyboard)

#включаем бота
bot.polling()
