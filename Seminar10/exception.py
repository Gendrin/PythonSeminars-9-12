# Думаем какие исключения реализовываем
# 1. Деление на ноль
# 2. Ввод символа заместо цифры или ,
#
#
def CheckInputFloat(testInput):
    try:
        return float(testInput)
    except ValueError:
        #print('Incorrect data entry')
        return None

def ChekInputZero(testInput):
    if testInput == 0:
        #print('Input zero, incorrect data entry!')
        return None
    else:
        return testInput
