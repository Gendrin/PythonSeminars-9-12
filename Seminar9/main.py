# This is a sample Python script.
import emoji
from isOdd import isOdd
from config import Token
from bot_commands import *



# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    print(Token())
    print(emoji.emojize('Python is :thumbs_up:'))
    print(isOdd(1))

    app = ApplicationBuilder().token(Token()).build()

    app.add_handler(CommandHandler("hi", hi_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("time", time_command))
    app.add_handler(CommandHandler("sum", sum_command))
    # Получение сообщений от юзера
    # @app.message_handler(content_types=["text"])
    # def handle_text(message):
    #     app.send_message(message.chat.id, 'Вы написали: ' + message.text)

    app.run_polling()

