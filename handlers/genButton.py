import math


class GenButtons:

    @classmethod
    async def inline_b(cls, l_text: list, l_value: list, row_w: int = 1, **kwargs) -> dict:
        """Generate custom inline button"""
        callback = 'callback_data'
        if kwargs.get('url', False) is True:
            callback = 'url'
        len_list = len(l_text)
        row_q = math.ceil(len_list / row_w)
        l_dict = [{"text": text, callback: value} for text, value in zip(l_text, l_value)]
        return {"row_wight": row_w, "inline_keyboard": cls.__json(l_dict, row_q, row_w)}

genButton = GenButtons()