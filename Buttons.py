from telegram import  ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton


def phone_button():
    button = [
        [KeyboardButton('raqamni yuborish', request_contact=True)]
    ]
    return ReplyKeyboardMarkup(button, resize_keyboard=True, one_time_keyboard=True)