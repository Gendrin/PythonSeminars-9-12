import telebot
import Test5 as ts5

# Создаем экземпляр бота
bot = telebot.TeleBot('5664442295:AAGp5Zv0mdVbKJCwRqd9Fc3qdI3zUobl-UM')

# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Я на связи. Напиши мне что-нибудь )')

@bot.message_handler(commands=["game"])
def start(m, res=False):
    bot.send_message(m.chat.id,ts5.draw_board(ts5.board))
    bot.send_message(m.chat.id, 'Выберите число вашего хода!')
# Получение сообщений от юзера

# def Pole():
#     bot.send_message(m.chat.id, ts5.draw_board(ts5.board))

@bot.message_handler(content_types=["text"])
def handle_text(message):
    listStep=['1','2','3','4','5','6','7','8','9']
    if message.text in listStep:
        bot.send_message(message.chat.id, 'Вы написали: ' + message.text)
# Запускаем бота
bot.polling(none_stop=True, interval=0)