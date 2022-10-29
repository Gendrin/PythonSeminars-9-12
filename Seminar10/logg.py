from datetime import datetime as dt


# Создаем файл лога если не создан
# Формирование строки записи в лог - время, операция, значения, результат
# Думаем над исключениями , - как минимм отработать деление на ноль
#
def inStringLog(inString):
    with open('log.txt', 'a', encoding='utf-8') as flog:
        inStr = dt.now().strftime('%D %H:%M')+' '+inString+'\n'
        flog.write(inStr)
    flog.close


