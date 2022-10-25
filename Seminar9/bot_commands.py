from telegram import Update
#from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes
import datetime
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackContext
)

def hi_command(update: Update, context: CallbackContext):
    update.message.reply_text(f'Hello {update.effective_user.first_name}')

def help_command(update: Update, context: CallbackContext):
    update.message.reply_text(f'/hi\n/time\n/help\n')

def time_command(update: Update, context: CallbackContext):
    update.message.reply_text(f'{datetime.datetime.now().time()}')

def sum_command(update: Update, context: CallbackContext):
    msg=update.message.text
    strList=msg.split()
    x=int(strList[1])
    y=int(strList[2])
    update.message.reply_text(f'x={x} y={y} x+y={x+y}')

# async def start(update: Update, _):
#     user=update.message.from_user
#     await update.message.reply_text(f'{user}')