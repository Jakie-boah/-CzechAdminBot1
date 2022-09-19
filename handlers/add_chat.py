from aiogram.types import Message
from config import dp, bot, greeting_in_chat
from i18.Localization import _
from Database.Database import TablesModerate


tables = TablesModerate()


@dp.message_handler(regexp='/start@A_not_herBot_bot')
async def f(message: Message):

    await message.answer(_(greeting_in_chat), disable_web_page_preview=True)

    id_chat_tg = message.chat.id
    title = message.chat.title
    chat_members_count = await bot.get_chat_members_count(message.chat.id)
    tables.add_new_chat(id_chat_tg, title, chat_members_count)
    await message.delete()















