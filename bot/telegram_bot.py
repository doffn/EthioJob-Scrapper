import telebot
from config import TELEGRAM_BOT_TOKEN

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

def send_report(message, chat_id):
    try:
        bot.send_message(chat_id=chat_id, text=message, parse_mode="Markdown")
    except Exception as e:
        print(f"Failed to send message: {e}")
        bot.send_message(chat_id=chat_id, text=message)
