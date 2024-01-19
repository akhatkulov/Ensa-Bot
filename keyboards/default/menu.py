from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
    [
        KeyboardButton(text="©️ Username")

    ],
    [
        KeyboardButton(text="🎞 Kino"),
        KeyboardButton(text="🌐 Domen")
    ],
    [
        KeyboardButton(text="🌦 Ob-havo"),
        KeyboardButton(text="📿 Nomoz Vaqti"),
        KeyboardButton(text="💸 Kurs")
    ],
    [
        KeyboardButton(text="💬 Bog'lanish")
    ],
    ],
    resize_keyboard= True
)