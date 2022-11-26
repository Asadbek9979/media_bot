from aiogram.dispatcher.filters import Text, Command
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, Message
from loader import dp,bot
from keyboards.default.aptekaa import menu

@dp.message_handler(Command("menu"))
async def show_menu(message: Message):
    await message.answer("Kurslar Tanlang", reply_markup=menu)
    