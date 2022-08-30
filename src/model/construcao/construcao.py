from __future__ import annotations
from ..objeto import Objeto

class Construcao(Objeto):

    def __init__(self: Construcao,valor_pedra: int, valor_madeira: int, x: int = 0, y: int = 0) -> None:
        super(Construcao, self).__init__(x, y)
        self.valor_pedra = valor_pedra
        self.valor_madeira = valor_madeira
