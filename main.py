from aiogram import executor
from filters.filters import IsAdmin, SuperAdmin
from config import dp
from Database.Database import CreateTables
import bot
import handlers.subscription
import handlers.mute_handler
import handlers.SuperAdmin
if __name__ == '__main__':
    CreateTables()
    dp.filters_factory.bind(SuperAdmin)
    dp.filters_factory.bind(IsAdmin)
    executor.start_polling(dp)
