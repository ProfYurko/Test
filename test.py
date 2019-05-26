import telebot

bot = telebot.TeleBot("821941732:AAFJDubxWcFuxaBmusWeZFq1B-rAAdRmjhg")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.send_message(message.chat.id, "ЕЙ, я вмію тільки повторяти за тобою)))")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.send_message(message.chat.id, message.text)

bot.polling(none_stop = True)