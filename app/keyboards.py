from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from config.config import operator_username


main = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Чат с оператором 💬')]
    ],
    resize_keyboard=True
)

help_url = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Чат с оператором', callback_data=f'url="https://t.me/{operator_username}')]
    ]
)