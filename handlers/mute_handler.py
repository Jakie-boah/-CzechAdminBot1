from aiogram.types import Message
from i18.Localization import _
from handlers.mute_config import MuteModerator
from filters.filters import IsAdmin
from config import dp, bot
from aiogram.dispatcher.filters import Command
from setups.mute_date import mute_date_calc
from aiogram.utils import exceptions

mute_mode = MuteModerator()


@dp.message_handler(Command("ban", prefixes='!'), IsAdmin())
async def ban(message: Message):
    if message.reply_to_message:
        try:
            time = await mute_date_calc(message.text)
            await mute_mode.mute_for_sometime(message.chat.id, message.reply_to_message.from_user['id'], time['until_date'])
            await message.reply(_(f'Пидормот {message.reply_to_message.from_user["username"]} забанен\nБан до {time["until_date"]}'))
        except IndexError:
            await message.reply(_('Упс, похоже вы ошиблись и добавили нужную информацию не полностью'))
    else:
        await message.reply("Вы должны применить команду на сообщение!")


@dp.message_handler(Command("unmute", prefixes='!'), IsAdmin())
async def unmute(message: Message):
    try:
        await mute_mode.unmute_member(message.chat.id, message.reply_to_message.from_user['id'])
        await message.reply(f"Пользователь {message.reply_to_message.from_user['username']} размучен")
    except exceptions.BadRequest as ex:
        await message.answer("У меня не получилось это сделать", ex)


@dp.message_handler(Command('massban', prefixes='!'), IsAdmin())
async def massban(message: Message):
    if message.reply_to_message:
        await mute_mode.massban(message.from_user.id)
        await message.reply(_(f'Пользователь {message.from_user.full_name} забанен везде'))
    else:
        await message.reply(_("Вы должны применить команду на сообщение!"))
