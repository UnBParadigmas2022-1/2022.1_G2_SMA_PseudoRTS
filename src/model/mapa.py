from __future__ import annotations
from .objeto import Objeto
from .construcao.construcao import Construcao
from .natural.pedra import Pedra
from .natural.arvore import Arvore
from utils.utils import posicao_aleatoria

class Mapa():
    def __init__(self: Mapa, y_tam: int, x_tam: int) -> None:
        self.grid = [object] * x_tam
        self.recursos = []
        self.construcao = []
        for i in range(x_tam):
            self.grid[i] = [object] * y_tam

    def preenche_mapa(self: Mapa, itens: int):
        for i in range(1, itens):
            x = posicao_aleatoria()
            y = posicao_aleatoria()
            arvore = Arvore(x, y)
            self.recursos.append(arvore)
            self.grid[x][y] = arvore

            x = posicao_aleatoria()
            y = posicao_aleatoria()
            pedra = Pedra(x, y)
            self.recursos.append(pedra)
            self.grid[x][y] = pedra

    def get_recursos(self: Mapa):
        return self.recursos

    def remove_recursos(self: Mapa, recurso: Natural) -> None:
        self.grid[recurso.x][recurso.y] = object
        self.recursos.remove(recurso)

    def set_construcao(self: Mapa, construcao: Construcao) -> None:
        self.construcao.append(construcao)
        self.grid[construcao.x][construcao.y] = construcao

    def is_posicao_vazia(self: Mapa, x: int, y: int) -> bool:
        if not isinstance(self.grid[x][y], Objeto):
            return True
        return False
    
    def is_posicao(self: Mapa, x: int, y: int) -> bool:
        if x < len(self.grid) and x >= 0 and y < len(self.grid[0]) and y >= 0:
            return True
        return False   
