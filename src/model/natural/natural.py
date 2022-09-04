from __future__ import annotations
from ..objeto import Objeto

class Natural(Objeto):

    def __init__(self: Natural, valor: int, x: int = 0, y: int = 0, shape: str = 'assets/image.png') -> None:
        super(Natural, self).__init__(x, y, shape)
        self.valor = valor
