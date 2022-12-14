from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from i18.Localization import _
from Database.Database import Database

CHOSEN_CHAT = []
CHATS = []
CHAT_LIST = Database().get_chats()


class InlineButtons:

    def introduce(self):
        markup = InlineKeyboardMarkup(row_width=1)
        add_chat = InlineKeyboardButton((_('Добавить чат')), callback_data='add_chat')
        buy_subscription = InlineKeyboardButton((_('Купить подписку')), callback_data='buy_subscription')
        return markup.add(add_chat, buy_subscription)

    def chat_list(self):
        c = 0
        markup = InlineKeyboardMarkup(row_width=1)
        if len(Database().get_chats()) == 0:
            empty = InlineKeyboardButton((_('Вы пока еще не добавили ни одного чата')), callback_data='empty')
            add_chat = InlineKeyboardButton((_('Добавить чат')), callback_data='empty')
            markup.add(empty, add_chat)
            return markup
        for i in Database().get_chats():
            markup.add(InlineKeyboardButton(i, callback_data=f'chat{c}'))
            c += 1
        confirm = InlineKeyboardButton((_('Подтвердить')), callback_data='confirm')
        markup.add(confirm)
        return markup

    def edit(self, number):
        c = 0
        for i in CHAT_LIST:
            if c == number:
                cur = Database().get_chats()[number].split()
                # if cur.split()[0] == '✅':
                #     cur.pop(0)
                # else:
                v = 0
                cure = ''
                for i in cur:
                    if v == 0:
                        cure = '✅ ' + i
                        v += 1
                    else:
                        cure += ' ' + i
                CHAT_LIST[number] = cure
                CHOSEN_CHAT.append(CHAT_LIST[number])
                CHATS.append(cure)
            else:
                CHATS.append(i)
            c += 1

    def new_inline(self):
        markup = InlineKeyboardMarkup(row_width=1)
        c = 0
        for k in CHAT_LIST:

            if k.split()[0] == '✅':
                markup.add(InlineKeyboardButton(k, callback_data=f'chosen_chat{c}'))
                # CHOSEN_CHAT.append(k)
                c += 1
            else:
                markup.add(InlineKeyboardButton(k, callback_data=f'chat{c}'))
                c += 1

        confirm = InlineKeyboardButton((_('Подтвердить')), callback_data='confirm')
        markup.add(confirm)
        return markup

    def offers(self):
        markup = InlineKeyboardMarkup(row_width=2)
        for_30 = InlineKeyboardButton((_('30 дней')), callback_data='for_30')
        for_90 = InlineKeyboardButton((_('90 дней')), callback_data='for_90')
        for_180 = InlineKeyboardButton((_('180 дней')), callback_data='for_180')
        for_365 = InlineKeyboardButton((_('365 дней')), callback_data='for_365')
        cancel = InlineKeyboardButton((_('Отменить')), callback_data='cancel')
        markup.add(for_30, for_90, for_180, for_365, cancel)
        return markup

    def confirm(self):
        markup = InlineKeyboardMarkup(row_width=1)
        confirm = InlineKeyboardButton((_('Подтвердить')), callback_data='CONFIRM')
        cancel = InlineKeyboardButton((_('Отменить')), callback_data='cancel')
        markup.add(confirm, cancel)
        return markup

    def pay(self):
        markup = InlineKeyboardMarkup(row_width=1)
        pay = InlineKeyboardButton((_('Оплатить')), callback_data='pay')
        cancel = InlineKeyboardButton((_('Отменить')), callback_data='cancel')
        markup.add(pay, cancel)
        return markup

    def add_chat(self):
        markup = InlineKeyboardMarkup(row_width=1)
        add = InlineKeyboardButton((_('Добавить')), url='https://t.me/A_not_herBot_bot?startgroup=c', callback_data='add')
        cancel = InlineKeyboardButton((_('Отменить')), callback_data='cancel')
        markup.add(add, cancel)
        return markup
# https://t.me/all2all_bot?startgroup=c