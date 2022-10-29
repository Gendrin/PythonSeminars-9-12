import logging

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
)

# Включим ведение журнала
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

# Определяем константы этапов разговора
CHECKM1,RMENU, CMENU, LOCATION, BIO = range(5)

# функция обратного вызова точки входа в разговор
def start(update, _):
    # Список кнопок для ответа
    reply_keyboard = [['1', '2']]
    # Создаем простую клавиатуру для ответа
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    # Начинаем разговор с вопроса
    update.message.reply_text(
        'Calculator welcomes you!\n\n\n'
        'Working with:\n'
        '1 - rational\n'
        '2 - complex\n'
        'Команда /cancel, чтобы выйти.\n\n',
        reply_markup=markup_key,)
    # переходим к этапу `GENDER`, это значит, что ответ
    # отправленного сообщения в виде кнопок будет список
    # обработчиков, определенных в виде значения ключа `GENDER`
    inText=update.message.text
    return CHECKM1

def checkStartMenu(update, _):
    inText = update.message.text
    reply_keyboardR = [['1', '2', '3', '4', '5', '6', '0']]
    reply_keyboardC = [['1', '2', '3', '4', '0']]
    markup_keyR = ReplyKeyboardMarkup(reply_keyboardR, one_time_keyboard=True)
    markup_keyC = ReplyKeyboardMarkup(reply_keyboardC, one_time_keyboard=True)
    if inText=='1':
        update.message.reply_text(
            'Operations rational number:\n'
            '1 - sum Сложение\n'
            '2 - sub Вычитание\n'
            '3 - mul Умножение\n'
            '4 - div Деление\n'
            '5 - pow Возведение в степень\n'
            '6 - sqrt Квадратный корень\n'
            '0 - previos menu\n',
            reply_markup=markup_keyR,
        )
        return RMENU
    if inText == '2':
        update.message.reply_text(
            'RRRRRRRRRRRRRRRRRRRRRRr:\n'
            '1 - sum Сложение\n'
            '2 - sub Вычитание\n'
            '3 - mul Умножение\n'
            '4 - div Деление\n'
            '5 - pow Возведение в степень\n'
            '6 - sqrt Квадратный корень\n'
            '0 - previos menu\n',
            reply_markup=markup_keyR,
        )
        #return CHECKM1
        return CMENU
    # else:
    #     if inText=='2':
    #         update.message.reply_text(
    #             'Operations complex number:\n'
    #             '1 - sum Сложение\n'
    #             '2 - sub Вычитание\n'
    #             '3 - mul Умножение\n'
    #             '4 - div Деление\n',
    #             '0 - previos menu\n',
    #             reply_markup=markup_keyC,
    #         )
    #         return Rational_Menu
        #return Complex_menu



def drat_menu(update, _):
    inText = update.message.text
    # Список кнопок для ответа
    reply_keyboard = [['1', '2','3','4','5','6','0']]
    # Создаем простую клавиатуру для ответа
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    # определяем пользователя
    user = update.message.from_user
    # Пишем в журнал пол пользователя
    logger.info("Пол %s: %s", user.first_name, update.message.text)
    # Следующее сообщение с удалением клавиатуры `ReplyKeyboardRemove`
    update.message.reply_text(
        'Рациональные вычисления:\n'
        '1 - sum Сложение\n'
        '2 - sub Вычитание\n'
        '3 - mul Умножение\n'
        '4 - div Деление\n'
        '5 - pow Возведение в степень\n'
        '6 - sqrt Квадратный корень\n'
        '0 - previos menu\n',
        reply_markup=markup_key,
    )
    # переходим к этапу `PHOTO`
    return CHECKM1

def dcomp_menu(update,_):
    inText = update.message.text
    # Список кнопок для ответа
    reply_keyboard = [['1', '2', '3', '4', '5', '6', '0']]
    # Создаем простую клавиатуру для ответа
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    # определяем пользователя
    user = update.message.from_user
    # Пишем в журнал пол пользователя
    logger.info("Пол %s: %s", user.first_name, update.message.text)
    # Следующее сообщение с удалением клавиатуры `ReplyKeyboardRemove`
    update.message.reply_text(
        'Комплексные вычисления\n'
        '1 - sum Сложение\n'
        '2 - sub Вычитание\n'
        '3 - mul Умножение\n'
        '4 - div Деление\n'
        '5 - pow Возведение в степень\n'
        '6 - sqrt Квадратный корень\n'
        '0 - previos menu\n',
        reply_markup=markup_key,
    )
    # переходим к этапу `PHOTO`
    if update.message.text == '0':
        return Start




# Обрабатываем фотографию пользователя
def photo(update, _):
    # определяем пользователя
    user = update.message.from_user
    # захватываем фото
    photo_file = update.message.photo[-1].get_file()
    # скачиваем фото
    photo_file.download(f'{user.first_name}_photo.jpg')
    # Пишем в журнал сведения о фото
    logger.info("Фотография %s: %s", user.first_name, f'{user.first_name}_photo.jpg')
    # Отвечаем на сообщение с фото
    update.message.reply_text(
        'Великолепно! А теперь пришли мне свое'
        ' местоположение, или /skip если параноик..'
    )
    # переходим к этапу `LOCATION`
    return LOCATION

# Обрабатываем команду /skip для фото
def skip_photo(update, _):
    # определяем пользователя
    user = update.message.from_user
    # Пишем в журнал сведения о фото
    logger.info("Пользователь %s не отправил фото.", user.first_name)
    # Отвечаем на сообщение с пропущенной фотографией
    update.message.reply_text(
        'Держу пари, ты выглядишь великолепно! А теперь пришлите мне'
        ' свое местоположение, или /skip если параноик.'
    )
    # переходим к этапу `LOCATION`
    return LOCATION

# Обрабатываем местоположение пользователя
def location(update, _):
    # определяем пользователя
    user = update.message.from_user
    # захватываем местоположение пользователя
    user_location = update.message.location
    # Пишем в журнал сведения о местоположении
    logger.info(
        "Местоположение %s: %f / %f", user.first_name, user_location.latitude, user_location.longitude)
    # Отвечаем на сообщение с местоположением
    update.message.reply_text(
        'Может быть, я смогу как-нибудь навестить тебя!' 
        ' Расскажи мне что-нибудь о себе...'
    )
    # переходим к этапу `BIO`
    return BIO

# Обрабатываем команду /skip для местоположения
def skip_location(update, _):
    # определяем пользователя
    user = update.message.from_user
    # Пишем в журнал сведения о местоположении
    logger.info("User %s did not send a location.", user.first_name)
    # Отвечаем на сообщение с пропущенным местоположением
    update.message.reply_text(
        'Точно параноик! Ну ладно, тогда расскажи мне что-нибудь о себе...'
    )
    # переходим к этапу `BIO`
    return BIO

# Обрабатываем сообщение с рассказом/биографией пользователя
def bio(update, _):
    # определяем пользователя
    user = update.message.from_user
    # Пишем в журнал биографию или рассказ пользователя
    logger.info("Пользователь %s рассказал: %s", user.first_name, update.message.text)
    # Отвечаем на то что пользователь рассказал.
    update.message.reply_text('Спасибо! Надеюсь, когда-нибудь снова сможем поговорить.')
    # Заканчиваем разговор.
    return ConversationHandler.END

# Обрабатываем команду /cancel если пользователь отменил разговор
def cancel(update, _):
    # определяем пользователя
    user = update.message.from_user
    # Пишем в журнал о том, что пользователь не разговорчивый
    logger.info("Пользователь %s отменил разговор.", user.first_name)
    # Отвечаем на отказ поговорить
    update.message.reply_text(
        'Мое дело предложить - Ваше отказаться'
        ' Будет скучно - пиши.',
        reply_markup=ReplyKeyboardRemove()
    )
    # Заканчиваем разговор.
    return ConversationHandler.END


if __name__ == '__main__':
    # Создаем Updater и передаем ему токен вашего бота.
    updater = Updater("5664442295:AAGp5Zv0mdVbKJCwRqd9Fc3qdI3zUobl-UM")
    # получаем диспетчера для регистрации обработчиков
    dispatcher = updater.dispatcher

    # Определяем обработчик разговоров `ConversationHandler`
    # с состояниями GENDER, PHOTO, LOCATION и BIO
    conv_handler = ConversationHandler( # здесь строится логика разговора
        # точка входа в разговор
        entry_points=[CommandHandler('start', start)],
        # этапы разговора, каждый со своим списком обработчиков сообщений
        states={
            CHECKM1: [MessageHandler(Filters.regex('^(1|2|3|4|5|6|0)$'), checkStartMenu)],
            RMENU: [MessageHandler(Filters.regex('^(1|2)$'), drat_menu)],
            CMENU: [MessageHandler(Filters.regex('^(1|2)$'), dcomp_menu)]
            #CheckSM: [MessageHandler(Filters.regex('^(1|2)$'), checkStartMenu)],

        },
        # точка выхода из разговора
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    # Добавляем обработчик разговоров `conv_handler`
    dispatcher.add_handler(conv_handler)

    # Запуск бота
    updater.start_polling()
    updater.idle()