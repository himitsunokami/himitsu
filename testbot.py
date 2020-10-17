import telebot

bot = telebot.TeleBot('1309409051:AAH5pD71j1LR8BPZhic6R8Q0_got9IsCZLE')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Здравствуй, пользователь!')


bot.polling()
