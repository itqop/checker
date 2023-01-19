from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

BTN_HELLO = InlineKeyboardButton('Hello', callback_data='hello')
BTN_WIND = InlineKeyboardButton('Wind', callback_data='wind')


HELLO = InlineKeyboardMarkup().add(BTN_WIND, BTN_HELLO)
WIND = InlineKeyboardMarkup().add(BTN_HELLO)
SUN_TIME = InlineKeyboardMarkup().add(BTN_HELLO, BTN_WIND)
HELP = InlineKeyboardMarkup().add(BTN_HELLO, BTN_WIND)