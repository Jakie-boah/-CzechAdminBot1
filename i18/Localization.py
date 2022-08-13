from aiogram.contrib.middlewares.i18n import I18nMiddleware
from typing import Tuple, Any
from pathlib import Path
from aiogram.types import User
from config import dp

LANG_STORAGE = {}
LANGS = ["ru", "en"]

I18N_DOMAIN = "mybot"
BASE_DIR = Path(__file__).parent
LOCALES_DIR = BASE_DIR / "locales"


class Localization(I18nMiddleware):
    async def get_user_locale(self, action: str, args: Tuple[Any]) -> str:

        user: User = User.get_current()

        if LANG_STORAGE.get(user.id) is None:
            LANG_STORAGE[user.id] = "en"
        *_, data = args
        language = data['locale'] = LANG_STORAGE[user.id]
        return language


i18n = Localization(I18N_DOMAIN, LOCALES_DIR)
dp.middleware.setup(i18n)
_ = i18n.lazy_gettext
