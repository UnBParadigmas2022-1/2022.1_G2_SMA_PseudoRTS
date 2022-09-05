from __future__ import annotations
from .construcao import Construcao

class Predio(Construcao):

    def __init__(self: Predio, x: int = 0, y: int = 0) -> None:
        super(Predio, self).__init__(2, 4, x, y)
