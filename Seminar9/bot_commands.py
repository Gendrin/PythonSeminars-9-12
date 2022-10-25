from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes
import datetime

async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'/hi\n/time\n/help\n')

async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'{datetime.datetime.now().time()}')

async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg=update.message.text
    strList=msg.split()
    x=int(strList[1])
    y=int(strList[2])
    await update.message.reply_text(f'x={x} y={y} x+y={x+y}')

# async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text(f'{datetime.datetime.now().time()}')
