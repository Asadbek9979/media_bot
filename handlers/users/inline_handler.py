from aiogram import types
from loader import dp
from keyboards.inline.buy_car import car_keys

from keyboards.inline.courses import aiogram_keys, python_keys

from data.courses_python import inline_results_python


@dp.inline_handler(text="python")
async def python_query(query: types.InlineQuery):
    await query.answer(inline_results_python)


@dp.inline_handler(text="rasm")
async def photo_query(query: types.InlineQuery):
    await query.answer(
        results=[
            types.InlineQueryResultPhoto(
                id="005",
                photo_url="https://i1.wp.com/mohirdev.uz/wp-content/uploads/Telegram-bot.png",
                thumb_url="https://i1.wp.com/mohirdev.uz/wp-content/uploads/Telegram-bot.png",
                caption="<b>Mukammal Telegram Yot</b> kursi.",
                reply_markup=aiogram_keys
            ),
            types.InlineQueryResultPhoto(
                id="006",
                photo_url="https://i1.wp.com/mohirdev.uz/wp-content/uploads/Anvar-aka-python.png",
                thumb_url="https://i1.wp.com/mohirdev.uz/wp-content/uploads/Anvar-aka-python.png",
                caption="<b>Python Dasturlash Asoslari</b> kursi.",
                reply_markup=python_keys
            ),
            types.InlineQueryResultVideo(
                id="007",
                video_url="https://streamable.com/ryeff4",
                caption="Million dolarlik g'oya",
                description="Go'yalarning asl bahosi",
                title="Million 💲 g'oya ",
                thumb_url="https://i.imgur.com/bY2XasE.png",
                mime_type="video/mp4",  # video/mp4 yoki text/html
            ),
        ]
    )


@dp.inline_handler()
async def empty_query(query: types.InlineQuery):
    await query.answer(
        results=[
            types.InlineQueryResultArticle(
                id="kurs001",
                title="📍 Eng yaqin do'konni topish",
                input_message_content=types.InputTextMessageContent(
                    message_text="https://t.me/uitc_backend_grands",
                ),
                reply_markup = car_keys,
                url="https://t.me/uitc_backend_grand",	
                description="Aptekega O'tish"
            ),
            types.InlineQueryResultArticle(
                id="kurs002",
                title="📱 Kontakt ulashish",
                input_message_content=types.InputTextMessageContent(
                    message_text="📱 Kontakt ulashish",
                ),
                url="https://t.me/uitc_backend_grand",
                description="Django frameworkida Web dasturlar yaratishni o'rganamiz"
            ),
        ],
    )
