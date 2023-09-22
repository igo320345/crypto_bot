from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

def coin_list_keyboard(coin_list):
    builder = InlineKeyboardBuilder()
    for coin in coin_list:
        builder.row(InlineKeyboardButton(text = f'#{coin.rank} - {coin.name}\n', callback_data = f'coin_info_{coin.slug}'))
    builder.row(InlineKeyboardButton(text = 'Load more...', callback_data = 'load_more'))
    return builder.as_markup()