from aiogram.dispatcher.filters import Command
from config import dp
from filters.filters import SuperAdmin
from aiogram.types import Message
from Database.Database import TablesModerate, Database
from i18.Localization import _

tables = TablesModerate()


@dp.message_handler(Command(commands="add_admin", prefixes='!'), SuperAdmin())
async def add_to_admins(message: Message):
    try:
        if int(message.text.split()[1]) in Database().get_admins():
            await message.reply(_(f"Юзер уже и так админ!\n\nСписок админов: {Database().get_admins()}"))
        else:
            tables.add_new_admin(message.text.split()[1], message.text.split()[2])
            await message.reply(_(f"Админ успешно добавлен!\n\nСписок админов: {Database().get_admins()}"))
    except IndexError:
        await message.reply(_('Упс, похоже вы ошиблись и добавили нужную информацию не полностью'))

