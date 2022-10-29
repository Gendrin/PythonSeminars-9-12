from telegram.ext import Updater
from user_interface import TextRationalMenu as TRM
from user_interface import TextComplexMenu as TCM
from user_interface import TextDivMenu as TDM
from user_interface import TextStartMenu as TSM

status=0

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