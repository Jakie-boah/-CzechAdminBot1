from config import bot
from datetime import datetime, timedelta
from Database.Database import ALL_CHATS


class MuteModerator:

    async def mute_for_sometime(self, chat_id, user_id, time):
        TIME = []
        for i in time:
            TIME.append(i)
            if i == 'd':
                time_from_now = datetime.now() + timedelta(days=int(TIME[0]))
                await bot.ban_chat_member(chat_id, user_id, '{:%H:%M:%S}'.format(time_from_now))

            elif i == 'h':
                time_from_now = datetime.now() + timedelta(hours=int(TIME[0]))
                await bot.ban_chat_member(chat_id, user_id, '{:%H:%M:%S}'.format(time_from_now))

            elif i == 'm':
                time_from_now = datetime.now() + timedelta(minutes=int(TIME[0]))
                await bot.ban_chat_member(chat_id, user_id, '{:%H:%M:%S}'.format(time_from_now))

            elif i == 'forever':
                await bot.ban_chat_member(chat_id, user_id)

    async def unmute(self, chat_id, user_id):
        await bot.unban_chat_member(chat_id=chat_id, user_id=user_id)

    async def massban(self, user_id):
        for i in ALL_CHATS:
            await bot.ban_chat_member(i, user_id)
