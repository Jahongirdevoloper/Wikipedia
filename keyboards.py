from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

btn_1 = InlineKeyboardButton('1', callback_data='1')
btn_2 = InlineKeyboardButton('2', callback_data='2')
btn_3 = InlineKeyboardButton('3', callback_data='3')
btn_4 = InlineKeyboardButton('4', callback_data='4')
btn_5 = InlineKeyboardButton('5', callback_data='5')
btn_6 = InlineKeyboardButton('6', callback_data='6')
btn_7 = InlineKeyboardButton('7', callback_data='7')
btn_8 = InlineKeyboardButton('8', callback_data='8')
btn_9 = InlineKeyboardButton('9', callback_data='9')
btn_10 = InlineKeyboardButton('10', callback_data='10')
inline_kb = InlineKeyboardMarkup(inline_keyboard=[
    [btn_1, btn_2, btn_3, btn_4, btn_5],
    [btn_6, btn_7, btn_8, btn_9, btn_10]
])
