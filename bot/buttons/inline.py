from aiogram.utils.keyboard import InlineKeyboardBuilder


def make_inline(btns:list, size:list):
    ikb = InlineKeyboardBuilder()
    ikb.add(*btns)
    ikb.adjust(*size)
    return ikb.as_markup()