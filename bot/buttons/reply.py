from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.utils.i18n import gettext as _

from bot.handlers import main_router

language_text ="Language"

def make_reply(btns:list, size:list):
    rkb = ReplyKeyboardBuilder()
    rkb.add(*btns)
    rkb.adjust(*size)
    return rkb.as_markup(resize_keyboard=True)


def menu_buttons():
    menu = KeyboardButton(text=_("Asosiy menu:"))
    res = KeyboardButton(text=_("Restoran menyusi"))
    call_us = KeyboardButton(text=_("Biz bilan bog'lanish"))
    buttons = [menu, res, call_us]
    size = [1,2]
    return make_reply(buttons, size)


def res_menu_buttons():
    salads = KeyboardButton(text=_("Salatlar"))
    fast_food = KeyboardButton(text=_("Fast Food"))
    food = KeyboardButton(text=_("Issiq taomlar"))
    back = KeyboardButton(text=_("Orqaga (Asosiy menyuga qaytish)"))
    buttons = [salads, fast_food, food, back]
    size = [1,1,1,1]
    return make_reply(buttons, size)


def salads_buttons():
    sezar = KeyboardButton(text=_("Sezar salati"))
    olivye = KeyboardButton(text=_("Olivye salati"))
    back = KeyboardButton(text=_("Orqaga (Restoran menyusiga qaytish)"))
    buttons = [sezar, olivye, back]
    size = [1,1,1]
    return make_reply(buttons, size)

def fast_food_buttons():
    burger = KeyboardButton(text=_("Burger"))
    hot_dog = KeyboardButton(text=_("Hot-dog"))
    back = KeyboardButton(text=_("Orqaga (Restoran menyusiga qaytish)"))
    buttons = [burger, hot_dog, back]
    size = [1,1,1]
    return make_reply(buttons, size)

def hot_buttons():
    plow = KeyboardButton(text=_("Osh"))
    soup = KeyboardButton(text=_("Sho'rva"))
    back = KeyboardButton(text=_("Orqaga (Restoran menyusiga qaytish)"))
    buttons = [plow, soup, back]
    size = [1,1,1]
    return make_reply(buttons, size)


def language_buttons():
    return None