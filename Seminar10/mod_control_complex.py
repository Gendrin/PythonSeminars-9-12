import exception as exp

MENU_COMP_DIGIT='2'
COMPSUM,COMPSUB,COMPMUL,COMPDIV=range(4)


state_complex=['1','2','3','4']

def ControlInTextComplexMenu(update, context):
    # Operations
    global status
    text = update.message.text
    if status == MENU_COMP_DIGIT and text == '1':  # Сложение
        context.bot.send_message(chat_id=update.effective_chat.id, text='Операция сложения комплексных чисел\n' + \
                                                                        'Введите действительную часть первого числа:')
        status = 55
        return

    if status == 55:
        A = exp.CheckInputFloat(text)
        if A != None:
            context.bot.send_message(chat_id=update.effective_chat.id, text='Ввведите второе число.')
            status = 56
            return
        else:
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text='Вы ввели не числовое значение, повторите ввод!')
            return

    if status == 56:
        B = exp.CheckInputFloat(text)
        if B != None:
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text='Результат ' + str(A) + '+' + str(B) + ' = ' + str(sum(A, B)))
            status = MENU_COMP_DIGIT
            context.bot.send_message(chat_id=update.effective_chat.id, text=TRM())
            return
        else:
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text='Вы ввели не числовое значение, повторите ввод!')
            return