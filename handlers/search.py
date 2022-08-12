
from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from .state_machine import AppState

async def cmd_search(message: types.Message, state: FSMContext):
    await AppState.search.set()
    await message.answer("<b>Поиск vk.com</b>\n\n"
                         "Введите поисковый запрос:",
                         parse_mode="HTML")

def register_handlers_search(dp: Dispatcher):
    dp.register_message_handler(cmd_search, commands="search", state=AppState.initial)