# This is a sample Python script.
import telebot
import game as ts5
from config import Token
from logg import inStringLog as inLg
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Создаем экземпляр бота
bot = telebot.TeleBot(Token())
startGame=False
count_step=1

@bot.message_handler(commands=["help"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'На данный момент у меня есть три команды:\n /game\n /start\n /help\n')
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
    inLg('Запущена новая игра!')
    ts5.init_board()
    bot.send_message(m.chat.id,ts5.draw_board(ts5.board))
    bot.send_message(m.chat.id, 'Выберите число вашего хода!')
    startGame=True

# Получение сообщений от юзера

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
                inLg('Игрок играющий за' +'"'+simbol+'"'+' выбрал поле -> '+message.text)
                win= ts5.check_win()
                if win:
                    bot.send_message(message.chat.id, 'Победили '+'"'+win+'"'+' игра окончена!')
                    inLg('Победили ' +'"'+win+'"'+' игра окончена!')
                    startGame=False
                if count_step==9:
                    bot.send_message(message.chat.id, 'Ничья игра окончена!')
                    inLg('Ничья игра окончена!')
                    startGame=False
                count_step+=1
            else:
                bot.send_message(message.chat.id, 'Это поле уже занято! ' + message.text)
                inLg('Попытка ввода уже занятого поля игроком играющим за '+'"'+simbol+'"'+' поле - '+message.text)
# Запускаем бота
bot.polling(none_stop=True, interval=0)


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
