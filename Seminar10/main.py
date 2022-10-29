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

updater = Updater(Token(), use_context=True)
# получаем экземпляр `Dispatcher`
dispatcher = updater.dispatcher

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    start_handler = CommandHandler('start', start)
    msg_handler = MessageHandler(Filters.text & (~Filters.command), ControlInText)
    msg_complex_handler=MessageHandler(Filters.text & (~Filters.command), mod_control_complex.ControlInTextComplexMenu)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(msg_handler)
    dispatcher.add_handler(msg_complex_handler)
    updater.start_polling()

