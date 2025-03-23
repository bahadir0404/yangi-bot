import telebot
from telebot import types

# Telegram bot sozlamalari
bot = telebot.TeleBot("YOUR_NEW_BO7659630694:AAHjQ77nuM0YsZUqXCn7iUlVCLVVi_u7b4wT_TOKEN")  # @BotFather’dan olingan tokenni shu yerga qo‘ying

# /start buyrug‘i uchun javob
@bot.message_handler(commands=['start'])
def send_welcome(message):
    chat_id = message.chat.id
    welcome_message = (
        "Assalomu alaykum! 👋\n"
        "Men yangi botman.\n"
        "Qanday yordam bera olaman?"
    )
    bot.send_message(chat_id, welcome_message)

# Botni ishga tushirish
if __name__ == "__main__":
    bot.polling(none_stop=True)