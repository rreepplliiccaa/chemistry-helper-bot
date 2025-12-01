import telebot
from telebot import types
from flask import Flask, request
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
if not TOKEN:
    raise ValueError("TELEGRAM_BOT_TOKEN не задан")

bot = telebot.TeleBot(TOKEN)

# Flask app для вебхука
app = Flask(__name__)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_channel_button(message):
    try:
        with open('./gggggg.jpg', 'rb') as photo:
            bot.send_photo(message.chat.id, photo)
    except FileNotFoundError:
        pass  # игнорируем, если фото нет на сервере

    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Открыть основной канал', url='https://t.me/chimicheskiy_nastavnik'))
    markup.add(types.InlineKeyboardButton('Репетиторы по химии', url='https://t.me/ChemistryTutor100'))
    bot.send_message(message.chat.id, 'Привет! Я твой помощник в подготовке к экзаменам и улучшении оценок по химии.', reply_markup=markup)

# Обработчик вебхука от Telegram
@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    if request.headers.get('content-type') == 'application/json':
        json_string = request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return 'OK', 200
    else:
        return 'Bad Request', 400

# Корень — для проверки
@app.route('/')
def index():
    return 'Telegram bot (webhook mode) is running!', 200

if __name__ == '__main__':
    # Установите вебхук при первом запуске (только локально!)
    # На Render этого делать НЕ нужно — там бот стартует как веб-сервер
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))