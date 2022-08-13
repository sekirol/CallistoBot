
from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from .state_machine import AppState

async def cmd_start(message: types.Message, state: FSMContext):
    await AppState.initial.set()
    await message.answer("Приветствую!")

async def cmd_cancel(message: types.Message, state: FSMContext):
    await state.finish()
    await message.reply('Действие отменено', reply_markup=types.ReplyKeyboardRemove())

def register_handlers_common(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands="start", state="*")
    dp.register_message_handler(cmd_cancel, commands="cancel", state="*")
    dp.register_message_handler(cmd_cancel, Text(equals="отмена", ignore_case=True), state="*")