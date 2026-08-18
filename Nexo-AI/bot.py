import telebot
from config import BOT_TOKEN
from ai import get_answer

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "🤖 Привет! Я Nexo AI.\n\n"
        "Я твой бесплатный ИИ-помощник.\n\n"
        "Напиши мне любой вопрос!"
    )


@bot.message_handler(commands=['help'])
def help_command(message):
    bot.send_message(
        message.chat.id,
        "🧠 Команды Nexo AI:\n\n"
        "/start — запуск бота\n"
        "/help — помощь\n\n"
        "Просто напиши сообщение, и я отвечу."
    )


@bot.message_handler(func=lambda message: True)
def answer(message):
    try:
        response = get_answer(message.text)
        bot.send_message(
            message.chat.id,
            response
        )

    except Exception as e:
        bot.send_message(
            message.chat.id,
            "❌ Ошибка: " + str(e)
        )


print("🤖 Nexo AI запущен!")

bot.infinity_polling()
