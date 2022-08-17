from aiogram import executor
from filters.filters import IsAdmin, SuperAdmin
from config import dp
from Database.Database import CreateTables
import bot
import handlers.subscription
import handlers.mute_handler
import handlers.SuperAdmin
import handlers.add_chat
if __name__ == '__main__':
    CreateTables()
    dp.filters_factory.bind(SuperAdmin)
    dp.filters_factory.bind(IsAdmin)
    executor.start_polling(dp)

#работа с бд!!! Когда юзер добавляет новый чат он должен залетать в бд!!! с нужной инфой!!!!
#добавить кнопки в главном боте, научить отклонять и действию назад
#пока как то так...