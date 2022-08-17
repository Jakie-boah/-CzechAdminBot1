from aiogram.types import CallbackQuery
from config import dp, bot, offers, days_amount
from Keyboards_assets.InlineButtons import CHOSEN_CHAT
from Keyboards_assets.InlineButtons import InlineButtons


@dp.callback_query_handler(text='add')
async def inline_kb_answer_callback_handler(query: CallbackQuery):
    print(query)
















