from loader import dp, bot
from aiogram.types import InputFile, Message, MediaGroup
from aiogram.dispatcher.filters import Command
from data.locations import Shops
from keyboards.inline.buy_car import car_keys

from loader import dp, bot

@dp.message_handler(Command("apteka"))
async def send_car(message: Message):
	text = "<b>APTEKA</b> bot\n"
	text += "Biz bilan topish oson\n"
	text += "Shu  Aptekalardan topish mumkin:\n"
	for i in Shops:
		text += i[0]+"\n"
	file_id = 'https://www.google.com/imgres?imgurl=https%3A%2F%2Fkeruencity.kz%2Fproducts%2F1516095027_34.JPG&imgrefurl=https%3A%2F%2Fkeruencity.kz%2Fproducts%2Fcvetnaya-apteka-1516095026&tbnid=QflP5I_BwORAOM&vet=12ahUKEwjs3MaE76_7AhUs17sIHQQ3CfYQMygjegUIARCpAg..i&docid=be5yiqXNvmEFyM&w=1024&h=663&q=%D0%B0%D0%BF%D1%82%D0%B5%D0%BA%D0%B0%20%D1%84%D0%BE%D1%82%D0%BE&ved=2ahUKEwjs3MaE76_7AhUs17sIHQQ3CfYQMygjegUIARCpAg'
	
	
	await message.reply_photo(file_id, caption=text, reply_markup=car_keys)
	
