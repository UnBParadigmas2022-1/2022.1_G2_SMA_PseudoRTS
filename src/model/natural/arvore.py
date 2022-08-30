from __future__ import annotations
from .natural import Natural
from random import randrange

class Arvore(Natural):

    def __init__(self: Arvore, x: int = 0, y: int = 0) -> None:
        super(Arvore, self).__init__(randrange(1, 6), x, y)
