from aiogram.types import Message, CallbackQuery
from handlers.mute_config import MuteModerator
from i18.Localization import _
from filters.filters import is_permitted
from config import dp, bot, greeting, buy_sub, instruction
from aiogram.dispatcher.filters import Command
from Database.Database import TablesModerate, Database
import asyncio
from setups.genButton import genButton
from Keyboards_assets.InlineButtons import InlineButtons
import handlers.add_chat
tables = TablesModerate()
mute_mode = MuteModerator()
is_permitted()

buttons = InlineButtons()


@dp.message_handler(Command(['start', 'help'], prefixes='!/'))
async def start(message: Message):
    await message.answer(_(greeting), disable_web_page_preview=True, reply_markup=buttons.introduce())
    await message.delete()


@dp.callback_query_handler(text='add_chat')
@dp.callback_query_handler(text='buy_subscription')
async def inline_kb_answer_callback_handler(query: CallbackQuery):
    answer_data = query.data
    # await query.answer(f'You answered with {answer_data!r}')

    if answer_data == 'add_chat':
        await query.message.edit_text(text=_(instruction), reply_markup=buttons.add_chat())

    elif answer_data == 'buy_subscription':
        await query.message.edit_text(text=_(buy_sub), reply_markup=buttons.chat_list())
    else:
        text = _(f'Не знаю что делать, возможно вы ошиблись в {answer_data!r}!')
        await query.message.edit_text(text=text)


@dp.callback_query_handler(regexp='chat')
async def choose(call: CallbackQuery):

    buttons.edit(int(call.data[-1]))
    await call.answer(cache_time=2)
    await call.message.edit_text(text=_(buy_sub), reply_markup=buttons.new_inline())


@dp.message_handler(Command('report', prefixes='!'))
async def report(message: Message):
    if message.reply_to_message:
        try:
            message_link = f"<a href='{message.reply_to_message.url}'>ссылка</a>"
            chat_name = message.chat.title
            text = f"<b>Поступил репорт:</b>\n<b>Чат:</b> {chat_name}\n<b>Сообщение:</b> {message_link}"

            for id_admin in Database().get_admins():
                b_text = ('Забанить', 'Мут', 'Удалить сообщение', 'Оставить')
                b_command = ('rep_ban', 'rep_mute', 'rep_del', 'rep_pass')
                rep_message_id = message.reply_to_message.message_id
                rep_user_id = message.reply_to_message.from_user.id
                rep_chat_id = message.reply_to_message.chat.id
                b_command = (f"{i} {rep_message_id} {rep_user_id} {rep_chat_id}" for i in b_command)
                buttons = await genButton.inline_b(b_text, b_command)

                await bot.send_message(id_admin, text, reply_markup=buttons)
                await bot.forward_message(id_admin, message.chat.id, message.reply_to_message.message_id)

        except Exception as err:
            for id_admin in Database().get_admins():
                await bot.send_message(id_admin, err)

        message_send = await message.answer(_("Жалоба принята!\nСпасибо за уведомление!"))
        await message.delete()

    else:
        message_send = await message.reply(_("Вы должны применить команду на сообщение!"))
    await asyncio.sleep(60)
    await message_send.delete()



