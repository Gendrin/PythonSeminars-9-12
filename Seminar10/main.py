# This is a sample Python script.
from telegram.ext import Updater
from config import Token
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
import mod_control_complex
from mod_control import ControlInText
from mod_control import start

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
status=0
fo=False #flagoperations
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
updater = Updater(Token(), use_context=True)
# получаем экземпляр `Dispatcher`
dispatcher = updater.dispatcher



def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    start_handler = CommandHandler('start', start)
    msg_handler = MessageHandler(Filters.text & (~Filters.command), ControlInText)
    msg_complex_handler=MessageHandler(Filters.text & (~Filters.command), mod_control_complex.ControlInTextComplexMenu)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(msg_handler)
    dispatcher.add_handler(msg_complex_handler)
    updater.start_polling()

