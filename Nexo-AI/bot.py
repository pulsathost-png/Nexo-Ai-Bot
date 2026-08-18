import telebot
from config import BOT_TOKEN

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "🤖 Привет! Я Nexo AI.\n\nЯ твой бесплатный ИИ-помощник."
    )

@bot.message_handler(func=lambda message: True)
def answer(message):
    bot.send_message(
        message.chat.id,
        "🧠 Nexo AI получил сообщение:\n" + message.text
    )

print("Nexo AI запущен!")

bot.infinity_polling()
