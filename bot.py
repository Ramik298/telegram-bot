import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Привет! Я работаю!')

if __name__ == '__main__':
    TOKEN = os.getenv('7533606845:AAE68NbF7DqB74UsyZJO2cgQGOl0Xk_z2-0')
    app = ApplicationBuilder().token(TOKEN).build()
    
    app.add_handler(CommandHandler('start', start))
    
    app.run_polling()
