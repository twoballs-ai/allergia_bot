from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def main_menu_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Добавить запись"),
                KeyboardButton(text="Просмотреть записи")
            ],
            [
                KeyboardButton(text="Настройки")
            ]
        ],
        resize_keyboard=True
    )
    return keyboard

def register_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Начать регистрацию")
            ]
        ],
        resize_keyboard=True
    )
    return keyboard

def cancel_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Отмена")
            ]
        ],
        resize_keyboard=True
    )
    return keyboard
