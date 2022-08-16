
from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext

from ..state_machine import AppState

async def cmd_search(message: types.Message, state: FSMContext):
    await state.set_state(AppState.search)

    await message.answer("<b>Поиск vk.com</b>\n\n"
                         "Введите поисковый запрос:",
                         parse_mode="HTML")

async def search_state_handler(message: types.Message, state: FSMContext):
    await message.answer("Ok")

def register_handlers_search(dp: Dispatcher):
    dp.register_message_handler(cmd_search, commands="search", state=AppState.initial)
    dp.register_message_handler(search_state_handler, state=AppState.search)