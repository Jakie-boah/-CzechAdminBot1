from aiogram.types import ChatPermissions

from config import bot
from datetime import datetime, timedelta
from Database.Database import ALL_CHATS



class MuteModerator:

    async def mute_for_sometime(self, chat_id, user_id, time):

        Ban_Premissions = ChatPermissions(
            can_send_messages=False,
            can_send_media_messages=False,
            can_send_polls=False,
            can_send_other_messages=False
        )

        TIME = []
        for i in time:
            TIME.append(i)
            if i == 'd':
                days_from_now = datetime.now() + timedelta(days=int(TIME[0]))
                await bot.restrict_chat_member(chat_id, user_id, permissions=Ban_Premissions, until_date='{:%H:%M:%S}'.format(days_from_now))

            elif i == 'h':
                hours_from_now = datetime.now() + timedelta(hours=int(TIME[0]))
                await bot.restrict_chat_member(chat_id, user_id, permissions=Ban_Premissions, until_date='{:%H:%M:%S}'.format(hours_from_now))

            elif i == 'm':
                minutes_from_now = datetime.now() + timedelta(minutes=int(TIME[0]))
                await bot.restrict_chat_member(chat_id, user_id, permissions=Ban_Premissions, until_date='{:%H:%M:%S}'.format(minutes_from_now))

            elif i == 'forever':
                await bot.ban_chat_member(chat_id, user_id)

    async def unmute(self, chat_id, user_id):

        Users_Premissions = ChatPermissions(
            can_send_messages=True,
            can_send_media_messages=True,
            can_send_polls=True,
            can_send_other_messages=True
        )

        await bot.restrict_chat_member(chat_id=chat_id, user_id=user_id, permissions=Users_Premissions, until_date=0)

    async def massban(self, user_id):
        Ban_Premissions = ChatPermissions(
            can_send_messages=False,
            can_send_media_messages=False,
            can_send_polls=False,
            can_send_other_messages=False
        )
        for i in ALL_CHATS:
            await bot.restrict_chat_member(i, user_id, permissions=Ban_Premissions)
