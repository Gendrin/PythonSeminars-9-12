# This is a sample Python script.
from telegram.ext import Updater
from config import Token
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from user_interface import TextStartMenu as TSM
from user_interface import TextRationalMenu as TRM
from user_interface import TextComplexMenu as TCM
from user_interface import TextDivMenu as TDM
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
status=0
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
updater = Updater(Token(), use_context=True)
# получаем экземпляр `Dispatcher`
dispatcher = updater.dispatcher

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,text=TSM())

def ControlInText(update, context):
    global status
    text = update.message.text
    if status==0 and text=='1':
        context.bot.send_message(chat_id=update.effective_chat.id, text=TRM())
        status+=1
    if status==0 and text=='2':
        context.bot.send_message(chat_id=update.effective_chat.id, text=TCM())
        status +=2
    if (status==1  or status==2) and text=='0':
        context.bot.send_message(chat_id=update.effective_chat.id, text=TSM())
        status=0
    if status==1 and text=='4':
        context.bot.send_message(chat_id=update.effective_chat.id, text=TDM())
        status = 3
    if status==3 and text=='0':
        context.bot.send_message(chat_id=update.effective_chat.id, text=TRM())
        status = 1

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    start_handler = CommandHandler('start', start)
    echo_handler = MessageHandler(Filters.text & (~Filters.command), ControlInText)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(echo_handler)

    updater.start_polling()

