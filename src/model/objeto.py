from __future__ import annotations

from mesa import Agent

class Objeto(Agent):

    def __init__(self: Objeto, x: int = 0, y: int = 0, shape: str = 'assets/image.png') -> None:
        self.x = x
        self.y = y
        self.shape = shape
