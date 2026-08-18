def get_answer(text):
    # Пока тестовый интеллект
    if "привет" in text.lower():
        return "Привет! Я Nexo AI 🤖"

    if "кто ты" in text.lower():
        return "Я Nexo AI — твой ИИ-помощник."

    return "Я пока учусь 🧠 Скоро буду отвечать умнее!"
