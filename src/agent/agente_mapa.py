from __future__ import annotations
from model.objeto import Objeto
from mesa import Agent
from model.natural.pedra import Pedra
from model.natural.arvore import Arvore
from utils.utils import posicao_aleatoria

class AgenteMapa(Objeto, Agent):
    def __init__(self: AgenteMapa, y_tam: int, x_tam: int) -> None:
        self.grid = [object] * x_tam
        self.recursos = []
        for i in range(x_tam):
            self.grid[i] = [object] * y_tam

    def preenche_mapa(self: AgenteMapa, itens: int):
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
        print(self.grid)

    def get_recursos(self: AgenteMapa):
        return self.recursos