from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.i18n import gettext as _
from aiogram.utils.i18n import lazy_gettext as __

from bot.buttons.reply import menu_buttons, language_text, language_buttons, res_menu_buttons, salads_buttons, \
    fast_food_buttons, hot_buttons
from bot.utils_function import save_user, check_user
from db.models import User

main_router = Router()
@main_router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await check_user(message)
    await message.answer(_("Hello, {}".format(message.from_user.full_name)), reply_markup=menu_buttons())


@main_router.message(F.text == __(language_text))
async def command_start_handler(message: Message) -> None:
    await message.answer(_("Choose language"), reply_markup=language_buttons())

@main_router.message(CommandStart())
async def command_handler(message: Message) -> None:
    await message.answer(_("Asosiy menu"), reply_markup=menu_buttons())

@main_router.message(CommandStart())
async def command_handler(message: Message) -> None:
    await message.answer(_("Restoran menyusi"), reply_markup=res_menu_buttons())


@main_router.message(CommandStart())
async def command_handler(message: Message) -> None:
    await message.answer(_("Salatlar"), reply_markup=salads_buttons())

@main_router.message(CommandStart())
async def command_handler(message: Message) -> None:
    await message.answer(_("Fast Food"), reply_markup=fast_food_buttons())

@main_router.message(CommandStart())
async def command_handler(message: Message) -> None:
    await message.answer(_("Fast Food"), reply_markup=hot_buttons())





# @main_router.message(BotState.language, F.text == __(main_text))
# @main_router.message(CommandStart())
# async def command_start_handler(message: Message) -> None:
#     await check_user(message)
#     await message.answer(_("Hello, {}! Please, choose the buttons!".format(message.from_user.full_name)),
#                          reply_markup=menu_buttons())
#
#
# @main_router.message(F.text == __(language_text))
# async def command_start_handler(message: Message, state: FSMContext) -> None:
#     await state.set_state(BotState.language)
#     await message.answer(_("Please, choose the language!"), reply_markup=language_buttons())
#
#
# @main_router.message(F.text == __(info_text))
# async def command_start_handler(message: Message):
#     await message.answer(_('''This bot is a bot that connects customers and developers.
# If you are a customer, it will select the application you need to create and direct you to the right developer.
# If you are a developer, post your work and find a customer.!'''), reply_markup=menu_buttons())
#
#
# @main_router.message(BotState.language, F.text.in_([uz_text, ru_text, en_text]))
# async def command_start_handler(message: Message, state: FSMContext, i18n) -> None:
#     map_ = {uz_text: "uz", ru_text: "ru", en_text: "en"}
#     await state.set_data({"locale": map_.get(message.text)})
#     i18n.current_locale = map_.get(message.text)
#     await message.answer(_("Please, choose the language!"), reply_markup=language_buttons())