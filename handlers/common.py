
from aiogram import Dispatcher, types

async def cmd_start(message: types.Message):
    await message.answer("Приветствую!")

def register_handlers_common(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands="start")