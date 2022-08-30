from __future__ import annotations
from .natural import Natural
from random import randrange

class Pedra(Natural):

    def __init__(self: Pedra, x: int = 0, y: int = 0) -> None:
        super(Pedra, self).__init__(randrange(1, 6), x, y)
