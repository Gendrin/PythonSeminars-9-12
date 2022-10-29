#from telegram.ext import Updater
import exception as exp
from user_interface import TextRationalMenu as TRM
from user_interface import TextComplexMenu as TCM
from user_interface import TextDivMenu as TDM
from user_interface import TextStartMenu as TSM
from model_sum import sum
from model_sub import sub
import model_mult
import model_div
from logg import inStringLog as lg


status=0

def start(update, context):
    global status
    context.bot.send_message(chat_id=update.effective_chat.id,text=TSM())
    status=0

def ControlInText(update, context):
    global status,A,B,A_CV,A_CM,B_CV,B_CM
    text = update.message.text
    # Movid from menu
    if status==0 and text=='1':
        context.bot.send_message(chat_id=update.effective_chat.id, text=TRM())
        status=1
        return
    if status==0 and text=='2':
        context.bot.send_message(chat_id=update.effective_chat.id, text=TCM())
        status=2
        return
    if (status==1  or status==2) and text=='0':
        context.bot.send_message(chat_id=update.effective_chat.id, text=TSM())
        status=0
        return
    if status==1 and text=='4':
        context.bot.send_message(chat_id=update.effective_chat.id, text=TDM())
        status = 3
        return
    if status==3 and text=='0':
        context.bot.send_message(chat_id=update.effective_chat.id, text=TRM())
        status = 1
        return

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
            resultStr='Результат сложения рациональных чисел '+str(A)+'+'+str(B)+' = '+str(sum(A,B))
            context.bot.send_message(chat_id=update.effective_chat.id, text=resultStr)
            lg(resultStr)
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
            resultStr= 'Результат вычитания рациональных чисел ' + str(A) + '-' + str(B) + ' = ' + str(sub(A, B))
            context.bot.send_message(chat_id=update.effective_chat.id,text=resultStr)
            lg(resultStr)
            status = 1
            context.bot.send_message(chat_id=update.effective_chat.id, text=TRM())
            return
        else:
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text='Вы ввели не числовое значение, повторите ввод!')
            return

    # Умножение
    if status == 1 and text == '3':  # вычитание
        context.bot.send_message(chat_id=update.effective_chat.id, text='Операция умножения чисел\n' + \
                                                                        'Введите первое число:')
        status = 44
        return

    if status == 44:
        A = exp.CheckInputFloat(text)
        if A != None:
            context.bot.send_message(chat_id=update.effective_chat.id, text='Ввведите второе число.')
            status = 45
            return
        else:
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text='Вы ввели не числовое значение, повторите ввод!')
            return

    if status == 45:
        B = exp.CheckInputFloat(text)
        if B != None:
            resultStr = 'Результат умножения рациональных чисел ' + str(A) + '*' + str(B) +' = ' \
                        + str(model_mult.mult(A, B))
            context.bot.send_message(chat_id=update.effective_chat.id, text=resultStr)
            lg(resultStr)
            status = 1
            context.bot.send_message(chat_id=update.effective_chat.id, text=TRM())
            return
        else:
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text='Вы ввели не числовое значение, повторите ввод!')
            return



# Возведение в степень  #################################################################

    if status == 1 and text == '5':  # степень
        context.bot.send_message(chat_id=update.effective_chat.id, text='Операция возведения в степень числа\n' + \
                                                                'Введите число:')
        status = 46
        return

    if status == 46:
        A = exp.CheckInputFloat(text)
        if A != None:
            context.bot.send_message(chat_id=update.effective_chat.id, text='Ввведите степень числа.')
            status = 47
            return
        else:
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text='Вы ввели не числовое значение, повторите ввод!')
            return

    if status == 47:
        B = exp.CheckInputFloat(text)
        if B != None:
            resultStr = 'Результат возведения в степень рационального числа ' + str(A) + ' в степень ' + str(B) + ' = ' \
                        + str(model_mult.dpow(A, B))
            context.bot.send_message(chat_id=update.effective_chat.id, text=resultStr)
            lg(resultStr)
            status = 1
            context.bot.send_message(chat_id=update.effective_chat.id, text=TRM())
            return
        else:
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text='Вы ввели не числовое значение, повторите ввод!')
            return


#   Квадратный корень ######################################################################

    if status == 1 and text == '6':  # корень
        context.bot.send_message(chat_id=update.effective_chat.id, text='Операция квадратный корень числа\n' + \
                                                                        'Введите число:')
        status = 48
        return

    if status == 48:
        A = exp.CheckInputFloat(text)
        if A != None:
            resultStr = 'Результат квадратного корня из ' + str(A)+' = ' \
                        + str(model_mult.dsqrt(A))
            context.bot.send_message(chat_id=update.effective_chat.id, text=resultStr)
            lg(resultStr)
            status = 1
            context.bot.send_message(chat_id=update.effective_chat.id, text=TRM())
            return
        else:
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text='Вы ввели не числовое значение, повторите ввод!')
            return

# Деление   ########################################################

    if status == 3 and text == '1':  # "/"
        context.bot.send_message(chat_id=update.effective_chat.id, text='Операция "/" деления чиселn\n' + \
                                                                        'Введите первое число:')
        status = 49
        return

    if status == 49:
        A = exp.CheckInputFloat(text)
        if A != None:
            context.bot.send_message(chat_id=update.effective_chat.id, text='Ввведите второе число.')
            status = 50
            return
        else:
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text='Вы ввели не числовое значение, повторите ввод!')
            return

    if status == 50:
        B = exp.CheckInputFloat(text)
        if B != None:
            if exp.ChekInputZero(B)!=None:
                resultStr = 'Результат деления рациональных чисел ' + str(A) + ' / ' + str(B) + ' = ' \
                            + str(model_div.div(A, B))
                context.bot.send_message(chat_id=update.effective_chat.id, text=resultStr)
                lg(resultStr)
                status = 3
                context.bot.send_message(chat_id=update.effective_chat.id, text=TDM())
                return
            else:
                resultStr = 'Второе число в операции деления равно 0, ошибка операции'
                context.bot.send_message(chat_id=update.effective_chat.id, text=resultStr)
                lg(resultStr)
                context.bot.send_message(chat_id=update.effective_chat.id, text='Повторите ввод второго числа!')
        else:
            context.bot.send_message(chat_id=update.effective_chat.id,
                                         text='Вы ввели не числовое значение, повторите ввод!')
            return
        # Целочисленное деление "//"

    if status == 3 and text == '2':  # "//"
        context.bot.send_message(chat_id=update.effective_chat.id, text='Операция "//" целочисленного деления чисел\n' + \
                                                                        'Введите первое число:')
        status = 51
        return

    if status == 51:
        A = exp.CheckInputFloat(text)
        if A != None:
            context.bot.send_message(chat_id=update.effective_chat.id, text='Ввведите второе число.')
            status = 52
            return
        else:
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text='Вы ввели не числовое значение, повторите ввод!')
            return

    if status == 52:
        B = exp.CheckInputFloat(text)
        if B != None:
            if exp.ChekInputZero(B) != None:
                resultStr = 'Результат целочисленного деления рациональных чисел ' + str(A) + ' // ' + str(B) + ' = ' \
                            + str(model_div.IntDiv(A, B))
                context.bot.send_message(chat_id=update.effective_chat.id, text=resultStr)
                lg(resultStr)
                status = 3
                context.bot.send_message(chat_id=update.effective_chat.id, text=TDM())
                return
            else:
                resultStr = 'Второе число в операции деления равно 0, ошибка операции'
                context.bot.send_message(chat_id=update.effective_chat.id, text=resultStr)
                lg(resultStr)
                context.bot.send_message(chat_id=update.effective_chat.id, text='Повторите ввод второго числа!')
        else:
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text='Вы ввели не числовое значение, повторите ввод!')
            return

    # Остаток от деления "%"

    if status == 3 and text == '3':  # "//"
        context.bot.send_message(chat_id=update.effective_chat.id, text='Операция "%" остатка от деления\n' + \
                                                                        'Введите первое число:')
        status = 53
        return

    if status == 53:
        A = exp.CheckInputFloat(text)
        if A != None:
            context.bot.send_message(chat_id=update.effective_chat.id, text='Ввведите второе число.')
            status = 54
            return
        else:
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text='Вы ввели не числовое значение, повторите ввод!')
            return

    if status == 54:
        B = exp.CheckInputFloat(text)
        if B != None:
            if exp.ChekInputZero(B) != None:
                resultStr = 'Результат остатка от деления рационального числа ' + str(A) + ' % ' + str(B) + ' = ' \
                            + str(model_div.RemDiv(A, B))
                context.bot.send_message(chat_id=update.effective_chat.id, text=resultStr)
                lg(resultStr)
                status = 3
                context.bot.send_message(chat_id=update.effective_chat.id, text=TDM())
                return
            else:
                resultStr = 'Второе число в операции деления равно 0, ошибка операции'
                context.bot.send_message(chat_id=update.effective_chat.id, text=resultStr)
                lg(resultStr)
                context.bot.send_message(chat_id=update.effective_chat.id, text='Повторите ввод второго числа!')
        else:
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text='Вы ввели не числовое значение, повторите ввод!')
            return

# Работа с комплексными числами
    if status == 2 and text == '1':  # Сложение
        context.bot.send_message(chat_id=update.effective_chat.id, text='Операция сложения комплексных чисел\n' + \
                                                                        'Введите действительную часть первого числа:')
        status = 55
        return

    if status == 55:
        A_CV = exp.CheckInputFloat(text)
        if A_CV != None:
            context.bot.send_message(chat_id=update.effective_chat.id, text='Ввведите мнимую часть первого числа.')
            status = 56
            return
        else:
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text='Вы ввели не числовое значение, повторите ввод!')
            return

    if status == 56:
        A_CM = exp.CheckInputFloat(text)
        if A_CM != None:
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text='Ввведите действительную часть второго числа')
            status = 57
            A = complex(A_CV,A_CM)
            return
        else:
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text='Вы ввели не числовое значение, повторите ввод!')
            return

    if status == 57:
        B_CV = exp.CheckInputFloat(text)
        if B_CV != None:
            context.bot.send_message(chat_id=update.effective_chat.id, text='Ввведите мнимую часть второго числа.')
            status = 58
            return
        else:
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text='Вы ввели не числовое значение, повторите ввод!')
            return

    if status == 58:
        B_CM = exp.CheckInputFloat(text)
        if B_CM != None:
            B = complex(B_CV, B_CM)
            context.bot.send_message(chat_id=update.effective_chat.id, text='Результат сложения А = '+str(A)\
                                                                        +' + B = '+str(B)+' = '+str(sum(A,B)))
            status = 2
            context.bot.send_message(chat_id=update.effective_chat.id, text=TCM())
            return
        else:
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text='Вы ввели не числовое значение, повторите ввод!')
            return
# Вычитание комплексного числа

    if status == 2 and text == '2':  # Вычитание
        context.bot.send_message(chat_id=update.effective_chat.id, text='Операция вычитания комплексных чисел\n' + \
                                                                        'Введите действительную часть первого числа:')
        status = 59
        return

    if status == 59:
        A_CV = exp.CheckInputFloat(text)
        if A_CV != None:
            context.bot.send_message(chat_id=update.effective_chat.id, text='Ввведите мнимую часть первого числа.')
            status = 60
            return
        else:
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text='Вы ввели не числовое значение, повторите ввод!')
            return

    if status == 60:
        A_CM = exp.CheckInputFloat(text)
        if A_CM != None:
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text='Ввведите действительную часть второго числа')
            status = 61
            A = complex(A_CV,A_CM)
            return
        else:
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text='Вы ввели не числовое значение, повторите ввод!')
            return

    if status == 61:
        B_CV = exp.CheckInputFloat(text)
        if B_CV != None:
            context.bot.send_message(chat_id=update.effective_chat.id, text='Ввведите мнимую часть второго числа.')
            status = 62
            return
        else:
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text='Вы ввели не числовое значение, повторите ввод!')
            return

    if status == 62:
        B_CM = exp.CheckInputFloat(text)
        if B_CM != None:
            B = complex(B_CV, B_CM)
            context.bot.send_message(chat_id=update.effective_chat.id, text='Результат вычитания А = '+str(A)\
                                                                        +' - B = '+str(B)+' = '+str(sub(A,B)))
            status = 2
            context.bot.send_message(chat_id=update.effective_chat.id, text=TCM())
            return
        else:
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text='Вы ввели не числовое значение, повторите ввод!')
            return

# Умножение комплексных чисел

    if status == 2 and text == '3':  # Умножение
        context.bot.send_message(chat_id=update.effective_chat.id, text='Операция умножения комплексных чисел\n' + \
                                                                        'Введите действительную часть первого числа:')
        status = 63
        return

    if status == 63:
        A_CV = exp.CheckInputFloat(text)
        if A_CV != None:
            context.bot.send_message(chat_id=update.effective_chat.id, text='Ввведите мнимую часть первого числа.')
            status = 64
            return
        else:
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text='Вы ввели не числовое значение, повторите ввод!')
            return

    if status == 64:
        A_CM = exp.CheckInputFloat(text)
        if A_CM != None:
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text='Ввведите действительную часть второго числа')
            status = 65
            A = complex(A_CV,A_CM)
            return
        else:
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text='Вы ввели не числовое значение, повторите ввод!')
            return

    if status == 65:
        B_CV = exp.CheckInputFloat(text)
        if B_CV != None:
            context.bot.send_message(chat_id=update.effective_chat.id, text='Ввведите мнимую часть второго числа.')
            status = 66
            return
        else:
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text='Вы ввели не числовое значение, повторите ввод!')
            return

    if status == 66:
        B_CM = exp.CheckInputFloat(text)
        if B_CM != None:
            B = complex(B_CV, B_CM)
            context.bot.send_message(chat_id=update.effective_chat.id, text='Результат умножения А = '+str(A)\
                                                            +' * B = '+str(B)+' = '+str(model_mult.mult(A,B)))
            status = 2
            context.bot.send_message(chat_id=update.effective_chat.id, text=TCM())
            return
        else:
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text='Вы ввели не числовое значение, повторите ввод!')
            return

# Деление комплексных чисел

    if status == 2 and text == '4':  # Деление
        context.bot.send_message(chat_id=update.effective_chat.id, text='Операция деления комплексных чисел\n' + \
                                                                        'Введите действительную часть первого числа:')
        status = 67
        return

    if status == 67:
        A_CV = exp.CheckInputFloat(text)
        if A_CV != None:
            context.bot.send_message(chat_id=update.effective_chat.id, text='Ввведите мнимую часть первого числа.')
            status = 68
            return
        else:
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text='Вы ввели не числовое значение, повторите ввод!')
            return

    if status == 68:
        A_CM = exp.CheckInputFloat(text)
        if A_CM != None:
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text='Ввведите действительную часть второго числа')
            status = 69
            A = complex(A_CV,A_CM)
            return
        else:
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text='Вы ввели не числовое значение, повторите ввод!')
            return

    if status == 69:
        B_CV = exp.CheckInputFloat(text)
        if B_CV != None:
            context.bot.send_message(chat_id=update.effective_chat.id, text='Ввведите мнимую часть второго числа.')
            status = 70
            return
        else:
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text='Вы ввели не числовое значение, повторите ввод!')
            return

    if status == 70:
        B_CM = exp.CheckInputFloat(text)
        if B_CM != None:
            B = complex(B_CV, B_CM)
            if exp.ChekInputZero(B) != None:
                resultStr = 'Результат деления комплексных чисел ' + str(A) + ' / ' + str(B) + ' = ' \
                            + str(model_div.div(A, B))
                context.bot.send_message(chat_id=update.effective_chat.id, text=resultStr)
                lg(resultStr)
                status = 2
                context.bot.send_message(chat_id=update.effective_chat.id, text=TDM())
                return
            else:
                resultStr = 'Второе число в операции деления равно 0, ошибка операции'
                context.bot.send_message(chat_id=update.effective_chat.id, text=resultStr)
                lg(resultStr)
                status=69
                context.bot.send_message(chat_id=update.effective_chat.id, text='Повторите ввод второго числа!\n'
                                                                    +'Введите действительую часть второго числа:')
        else:
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text='Вы ввели не числовое значение, повторите ввод!')
            return


