from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from i18.Localization import _


CHAT_LIST = ['Чат 1', 'Чат 2', 'Чат 3']

CHOSEN_CHAT = []


class InlineButtons:

    def introduce(self):
        markup = InlineKeyboardMarkup(row_width=1)
        add_chat = InlineKeyboardButton((_('Добавить чат')), callback_data='add_chat')
        buy_subscription = InlineKeyboardButton((_('Купить подписку')), callback_data='buy_subscription')
        return markup.add(add_chat, buy_subscription)

    def chat_list(self):
        c = 0
        markup = InlineKeyboardMarkup(row_width=1)
        for i in CHAT_LIST:
            markup.add(InlineKeyboardButton(i, callback_data=f'chat{c}'))
            c += 1
        confirm = InlineKeyboardButton((_('Подтвердить')), callback_data='confirm')
        markup.add(confirm)
        return markup

    def edit(self, number):
        c = 0
        for i in CHAT_LIST:
            if c == number:
                cur = CHAT_LIST[number]
                if cur.split()[0] == '✅':
                    pass
                else:
                    CHAT_LIST[number] = '✅ ' + cur
                    CHOSEN_CHAT.append(CHAT_LIST[number])
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
        markup.add(for_30, for_90, for_180, for_365)
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

