#!/usr/bin/python
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
API_TOKEN = '6804555696:AAHQ_XEv8z483jP0PlHB0eefjtEq-L5FIKw'

bot = telebot.TeleBot(API_TOKEN)

keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(KeyboardButton('A bout us?'))


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Hi! Mingalarpar!')
    bot.send_message(message.chat.id, "choose an option:",
                     reply_markup=keyboard)


@bot.message_handler(func=lambda message: True)
def echo_message(message):

    if 'A bout us?' in message.text:
        bot.reply_to(message, 'We are ChatBot')
    elif 'a bout us?' in message.text:
        bot.reply_to(message, 'We are ChatBot')
    else:
        if 'A bout us' in message.text:
            bot.reply_to(message, 'We are ChatBot')
        elif 'a bout us' in message.text:
            bot.reply_to(message, 'We are ChatBot')
############### End Name?#################
    if 'who are you?' in message.text:
        bot.reply_to(message, 'I am XXXX')
    elif 'Who are you?' in message.text:
        bot.reply_to(message, 'I am XXXX')
    else:
        if 'who are you' in message.text:
            bot.reply_to(message, 'I am XXXX')
        elif 'w r u?' in message.text:
            bot.reply_to(message, 'I am XXXX')
############### End Name?#################

    if 'How are you?' in message.text:
        bot.reply_to(message, 'I am good, you?')
    elif 'How are you' in message.text:
        bot.reply_to(message, 'I am good, you?')
    else:
        if 'how are you?' in message.text:
            bot.reply_to(message, 'I am good, you?')
        elif 'how are you' in message.text:
            bot.reply_to(message, 'I am good, you?')
############### End How are you?#################
    if 'Hi' in message.text:
        bot.reply_to(message, 'Hi')
    elif 'hi' in message.text:
        bot.reply_to(message, 'hi')
    else:
        if 'Hello' in message.text:
            bot.reply_to(message, 'Hello')
        elif 'hello' in message.text:
            bot.reply_to(message, 'hello')
############### End Say Hi?#################

    if 'OK' in message.text:
        bot.reply_to(message, 'Ok, Let start it!')
    elif 'Ok' in message.text:
        bot.reply_to(message, 'Ok, Let start it!')
    else:
        if 'ok' in message.text:
            bot.reply_to(message, 'Ok, Let start it!')
        elif 'oke' in message.text:
            bot.reply_to(message, 'Ok, Let start it!')
############### End Say Hi?#################
    if 'Gender' in message.text:
        bot.reply_to(message, 'Boy')
    elif 'boy' in message.text:
        bot.reply_to(message, 'Boy')
    else:
        if 'girl' in message.text:
            bot.reply_to(message, 'Boy')
        elif 'Boy' in message.text:
            bot.reply_to(message, 'Boy')
            ### Or####
    if 'Girl' in message.text:
        bot.reply_to(message, 'Boy')
    elif 'boi' in message.text:
        bot.reply_to(message, 'Boy')
    else:
        if 'male' in message.text:
            bot.reply_to(message, 'Boy')
        elif 'female' in message.text:
            bot.reply_to(message, 'Boy')
############### End Gender?#################

    if 'Phone' in message.text:
        bot.reply_to(message, '09XXXX')
    elif 'PH' in message.text:
        bot.reply_to(message, '09XXXX')
    else:
        if 'PHONE' in message.text:
            bot.reply_to(message, '09XXXX')
        elif 'TelePhone' in message.text:
            bot.reply_to(message, '09XXXX')
############### End Phone?#################

    if 'Address' in message.text:
        bot.reply_to(message, 'Yangon')
    elif 'address' in message.text:
        bot.reply_to(message, 'Yangon')
    else:
        if 'ADDRESS' in message.text:
            bot.reply_to(message, 'Yangon')
        elif 'ads' in message.text:
            bot.reply_to(message, 'Yangon')
############### End Address?#################


bot.infinity_polling()
