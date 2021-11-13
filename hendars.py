from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types.message import ContentType
from config import dp
import wikipedia
from aiogram.dispatcher.filters import CommandStart
from keyboards import inline_kb
from States import Article

@dp.message_handler(CommandStart())
async def starts(message:types.Message):
    await message.answer("Assalomu alaykum \nIltimos maqolani <b>Sarlavhasini kiriting</b> 👇")

@dp.message_handler()
async def article_list(message:types.Message, state:FSMContext):
    await Article.articles.set()
    wikipedia.set_lang('uz')
    data = wikipedia.search(message)
    if data:
        for dat in range(0, len(data)):
            await message.answer(f"<b>{dat+1}</b>.{data[dat]}")
        await message.answer("<b>Maqolarni tanlang 👇</b>\n", reply_markup=inline_kb)
    else:
        await message.answer("<b>Kechirasiz siz izlagan maqaola topipmadi\nQayta urinib 👇</b>")
    await state.update_data(article=data)

@dp.callback_query_handler(state=Article.articles)
async def send_random_value(call: types.CallbackQuery,state:FSMContext):
    num = int(call.data)-1
    data = await state.get_data()
    q = data.get('article')[num]
    wikipedia.set_lang('uz')
    data2 = wikipedia.summary(q)
    await call.message.answer(data2)
