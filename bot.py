import os
import telebot

# Получаем токен из переменной окружения
BOT_TOKEN = os.getenv('7533606845:AAE68NbF7DqB74UsyZJO2cgQGOl0Xk_z2-0')

if BOT_TOKEN is None:
    print("Ошибка: BOT_TOKEN не найден в переменных окружения.")
else:
    bot = telebot.TeleBot(BOT_TOKEN)

    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        # Пример объекта, который может быть неопределенным
        myObject = get_some_object()  # Это пример, замените на ваш реальный код

        # Добавление проверки на наличие объекта и его свойства id
        if myObject and 'id' in myObject:
            bot.send_message(message.chat.id, f"Привет! Твой ID: {myObject['id']}")
        else:
            bot.send_message(message.chat.id, "Не удалось получить ID объекта.")
    
    # Запуск бота
    bot.polling()

#
