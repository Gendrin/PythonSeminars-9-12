from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

def hello(update: Update, context: CaLLback) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')