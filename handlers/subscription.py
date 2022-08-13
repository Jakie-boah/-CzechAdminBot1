from aiogram.types import CallbackQuery
from config import dp, bot, offers, days_amount
from Keyboards_assets.InlineButtons import CHOSEN_CHAT
from Keyboards_assets.InlineButtons import InlineButtons


buttons = InlineButtons()


def tak():
    end = ''
    for i in CHOSEN_CHAT:
        end += i[1:] + ','
    return end


@dp.callback_query_handler(text='confirm')
async def inline_kb_answer_callback_handler(query: CallbackQuery):
    await bot.send_message(query.from_user.id, offers, reply_markup=buttons.offers())


@dp.callback_query_handler(regexp='for')
async def choose(call: CallbackQuery):
    days = int((call.data[-2] + call.data[-1]))
    if days == 30:
        await bot.send_message(call.from_user.id, days_amount(30, tak(), (169 * len(CHOSEN_CHAT))), reply_markup=buttons.confirm())
    elif days == 90:
        await bot.send_message(call.from_user.id, days_amount(90, tak(), (469 * len(CHOSEN_CHAT))), reply_markup=buttons.confirm())
    elif days == 180:
        await bot.send_message(call.from_user.id, days_amount(180, tak(), (849 * len(CHOSEN_CHAT))), reply_markup=buttons.confirm())
    elif days == 365:
        await bot.send_message(call.from_user.id, days_amount(365, tak(), (1579 * len(CHOSEN_CHAT))), reply_markup=buttons.confirm())


@dp.callback_query_handler(text='CONFIRM')
async def inline_kb_answer_callback_handler(query: CallbackQuery):
    await bot.send_message(query.from_user.id, 'Подтвердите покупку',
                           reply_markup=buttons.pay())















