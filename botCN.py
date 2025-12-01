import telebot
from telebot import types
from dotenv import load_dotenv
import os

load_dotenv()  # Загружает переменные из .env

TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
if not TOKEN:
    raise ValueError("Токен не найден! Проверьте файл .env")

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def send_channel_button(message):
    try:
        with open('./gggggg.jpg', 'rb') as photo:
            bot.send_photo(message.chat.id, photo)
    except FileNotFoundError:
        bot.send_message(message.chat.id, "Изображение не найдено.")

    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Открыть основной канал', url='https://t.me/chimicheskiy_nastavnik'))
    markup.add(types.InlineKeyboardButton('Репетиторы по химии', url='https://t.me/ChemistryTutor100'))

    bot.send_message(
        message.chat.id,
        'Привет! Я твой помощник в подготовке к экзаменам и улучшении оценок по химии.',
        reply_markup=markup
    )


bot.polling(none_stop=True)