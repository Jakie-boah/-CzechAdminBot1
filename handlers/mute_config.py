from aiogram.types import ChatPermissions
from config import bot
from datetime import datetime, timedelta
from Database.Database import Database

Ban_Premissions = ChatPermissions(
            can_send_messages=False,
            can_send_media_messages=False,
            can_send_polls=False,
            can_send_other_messages=False
        )
Users_Premissions = ChatPermissions(
            can_send_messages=True,
            can_send_media_messages=True,
            can_send_polls=True,
            can_send_other_messages=True
        )


class MuteModerator:

    async def mute_for_sometime(self, chat_id, user_id, time):
        await bot.restrict_chat_member(chat_id, user_id,
                                   permissions=Ban_Premissions,
                                   until_date=time)

    async def unmute_member(self, message):

        await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user['id'], permissions=Users_Premissions,
                                        until_date=0)

    async def massban(self, user_id):

        for i in Database().get_chats():
            await bot.restrict_chat_member(i, user_id, permissions=Ban_Premissions)
