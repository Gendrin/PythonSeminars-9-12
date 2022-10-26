import telebot
import Test5 as ts5

# Создаем экземпляр бота
bot = telebot.TeleBot('5664442295:AAGp5Zv0mdVbKJCwRqd9Fc3qdI3zUobl-UM')
startGame=False
count_step=1
# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Я на связи. Напиши мне что-нибудь )')

@bot.message_handler(commands=["game"])
def start(m, res=False):
    global count_step
    global startGame
    count_step=1
    bot.send_message(m.chat.id, 'Новая игра!!')
    ts5.init_board()
    bot.send_message(m.chat.id,ts5.draw_board(ts5.board))
    bot.send_message(m.chat.id, 'Выберите число вашего хода!')
    startGame=True

# Получение сообщений от юзера

# def Pole():
#     bot.send_message(m.chat.id, ts5.draw_board(ts5.board))

@bot.message_handler(content_types=["text"])
def handle_text(message):
    global startGame
    global count_step
    if startGame:
        listStep=['1','2','3','4','5','6','7','8','9']
        if message.text in listStep:
            #count_step += 1
            if count_step % 2 == 0: simbol = 'X'
            else:simbol = 'O'
            #bot.send_message(message.chat.id, 'Вы написали: ' + message.text)
            if ts5.tk_in(simbol,int(message.text))!=None:
                bot.send_message(message.chat.id, ts5.draw_board(ts5.board))
                win= ts5.check_win()
                if win:
                    bot.send_message(message.chat.id, 'Победили ' +win+' игра окончена!')
                    startGame=False
                if count_step==9:
                    bot.send_message(message.chat.id, 'Ничья игра окончена!')
                    startGame=False
                count_step+=1
            else:
                bot.send_message(message.chat.id, 'Это поле уже занято! ' + message.text)
# Запускаем бота
bot.polling(none_stop=True, interval=0)