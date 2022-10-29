from telegram.ext import Updater
import exception as exp
from user_interface import TextRationalMenu as TRM
from user_interface import TextComplexMenu as TCM
from user_interface import TextDivMenu as TDM
from user_interface import TextStartMenu as TSM
from model_sum import sum
from model_sub import sub

status=0

def start(update, context):
    global status
    context.bot.send_message(chat_id=update.effective_chat.id,text=TSM())
    status=0

def ControlInText(update, context):
    global status,A,B,fo
    text = update.message.text
    # Movid from menu
    if status==0 and text=='1':
        context.bot.send_message(chat_id=update.effective_chat.id, text=TRM())
        status=1
        return
    if status==0 and text=='2':
        context.bot.send_message(chat_id=update.effective_chat.id, text=TCM())
        status=2
    if (status==1  or status==2) and text=='0':
        context.bot.send_message(chat_id=update.effective_chat.id, text=TSM())
        status=0
    if status==1 and text=='4':
        context.bot.send_message(chat_id=update.effective_chat.id, text=TDM())
        status = 3
    if status==3 and text=='0':
        context.bot.send_message(chat_id=update.effective_chat.id, text=TRM())
        status = 1

    # Operations
    if status == 1 and text == '1': # Сложение
        context.bot.send_message(chat_id=update.effective_chat.id, text='Операция сложения чисел\n'+\
                                                                        'Введите первое число:')
        status=40
        return

    if status == 40:
        A=exp.CheckInputFloat(text)
        if A!=None:
            context.bot.send_message(chat_id=update.effective_chat.id, text='Ввведите второе число.')
            status=41
            return
        else:
            context.bot.send_message(chat_id=update.effective_chat.id,
                                    text='Вы ввели не числовое значение, повторите ввод!')
            return

    if status == 41:
        B=exp.CheckInputFloat(text)
        if B!=None:
            context.bot.send_message(chat_id=update.effective_chat.id, text='Результат '+str(A)+'+'+str(B)+'='+str(sum(A,B)))
            status=1
            context.bot.send_message(chat_id=update.effective_chat.id, text=TRM())
            return
        else:
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text='Вы ввели не числовое значение, повторите ввод!')
            return

    if status == 1 and text == '2':  # вычитание
        context.bot.send_message(chat_id=update.effective_chat.id, text='Операция вычитания чисел\n' + \
                                                                        'Введите первое число:')
        status = 42
        return

    if status == 42:
        A = exp.CheckInputFloat(text)
        if A != None:
            context.bot.send_message(chat_id=update.effective_chat.id, text='Ввведите второе число.')
            status = 43
            return
        else:
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text='Вы ввели не числовое значение, повторите ввод!')
            return

    if status == 43:
        B = exp.CheckInputFloat(text)
        if B != None:
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text='Результат ' + str(A) + '-' + str(B) + '=' + str(sub(A, B)))
            status = 1
            context.bot.send_message(chat_id=update.effective_chat.id, text=TRM())
            return
        else:
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text='Вы ввели не числовое значение, повторите ввод!')
            return



