from flask import Flask, request, Response
import requests
import telebot
import pytube

bot_token = '5407530364:AAFKc_kOuxKMv6NaXfOOA5UoLHfrU_v-6GE'
bot = telebot.TeleBot(bot_token, parse_mode=None)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message,'This is a real fucking bot that fucking converts youtube videos to fucking audio without stupid ads. By Nilu')
    bot.register_next_step_handler(message, convert)
    

@bot.message_handler(content_types=['url'], func=lambda message: True)
def convert(message):
    url = message.text
    bot.reply_to(message, 'Got the link.')
    chat_id = message.chat.id
    try:
        yt = pytube.YouTube(url)
        stream = yt.streams.filter(only_audio=True).first()
        stream.download()
        bot.reply_to(message, 'Downloaded')
        #send audio to user
        audio = open(stream.default_filename, 'rb' )
        yt.thumbnail_url
        #send mp3 to user
        bot.send_audio(chat_id, audio)
        bot.reply_to(message, 'Sent, you fucking cunt')
    except:
        bot.send_message(chat_id, 'Error')
    #continue accepting links
    bot.send_message(chat_id, 'Send me another link')
    bot.register_next_step_handler(message, convert)
    

bot.infinity_polling()