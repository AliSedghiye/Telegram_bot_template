import telebot
import os
import emoji
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

from db import MongoDB 


class Bot:
    def __init__(self):
        print("Initializing Bot...")
        self.bot = telebot.TeleBot(os.environ['PYTEL_TOKEN'])
        self.db = MongoDB()  # Initialize MongoDB connection
        self.echo_all = self.bot.message_handler(func=lambda m: True)(self.echo_all)
        self.start_handler = self.bot.message_handler(commands=['start'])(self.start)
        self.callback_handler = self.bot.callback_query_handler(func=lambda call: True)(self.handle_callback)

    def run(self):
        self.bot.infinity_polling()

    def get_main_markup(self):
        markup = InlineKeyboardMarkup()
        # Each button on its own row, with emoji using emoji library
        markup.add(
            InlineKeyboardButton(emoji.emojize(":gear: Setting"), callback_data="setting")
        )
        markup.add(
            InlineKeyboardButton(emoji.emojize(":test_tube: Test"), callback_data="test")
        )
        return markup

    def start(self, message):
        markup = self.get_main_markup()
        # Example: Save user info to MongoDB on /start
        users = self.db.get_collection('users')
        users.update_one(
            {'user_id': message.from_user.id},
            {'$set': {'username': message.from_user.username}},
            upsert=True
        )
        self.bot.reply_to(
            message,
            "Welcome! I'm your Telegram bot. How can I help you?",
            reply_markup=markup
        )

    def echo_all(self, message):
        markup = self.get_main_markup()
        self.bot.reply_to(message, message.text, reply_markup=markup)

    def handle_callback(self, call):
        if call.data == "setting":
            self.bot.answer_callback_query(call.id, "Settings button pressed!")
            self.bot.send_message(call.message.chat.id, "You pressed the Setting button.", reply_markup=self.get_main_markup())
        elif call.data == "test":
            self.bot.answer_callback_query(call.id, "Test button pressed!")
            self.bot.send_message(call.message.chat.id, "You pressed the Test button.", reply_markup=self.get_main_markup())


if __name__ == '__main__':
    but = Bot()
    but.run()