from __future__ import annotations
from .construcao import Construcao
class Casa(Construcao):

    def __init__(self: Casa, x: int = 0, y: int = 0) -> None:
        super(Casa, self).__init__(2, 6, x, y)
