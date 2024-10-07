from os import environ
from typing import Final


class TgKeys:
    TOKEN: Final = environ.get('TG_TOKEN', 'define me!')
