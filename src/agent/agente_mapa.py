from __future__ import annotations
from mesa import Agent, Model
from model.objeto import Objeto
from model.construcao.construcao import Construcao
from model.natural.pedra import Pedra
from model.natural.arvore import Arvore
from utils.utils import posicao_aleatoria

class AgenteMapa(Agent):
    def __init__(self: AgenteMapa, unique_id: int, model: "Model", y_tam: int, x_tam: int) -> None:
        self.unique_id = unique_id
        self.model = model
        self.grid_mapa = [object] * x_tam
        self.recursos = []
        self.construcao = []
        self.y_tam = y_tam
        self.x_tam = x_tam
        for i in range(x_tam):
            self.grid_mapa[i] = [object] * y_tam

    def preenche_mapa(self: AgenteMapa, itens: int):
        for i in range(0, itens):
            x = posicao_aleatoria(1, self.x_tam - 1)
            y = posicao_aleatoria(1, self.y_tam - 1)
            arvore = Arvore(x, y)
            self.recursos.append(arvore)
            self.grid_mapa[x][y] = arvore
            self.model.grid.place_agent(self, (x , y))

            x = posicao_aleatoria(1, self.x_tam - 1)
            y = posicao_aleatoria(1, self.y_tam - 1)
            pedra = Pedra(x, y)
            self.recursos.append(pedra)
            self.grid_mapa[x][y] = pedra
            self.model.grid.place_agent(self, (x , y))

    def get_recursos(self: AgenteMapa):
        return self.recursos

    def remove_recursos(self: AgenteMapa, recurso: Natural) -> None:
        self.grid_mapa[recurso.x][recurso.y] = object
        self.recursos.remove(recurso)

    def set_construcao(self: AgenteMapa, construcao: Construcao) -> None:
        self.construcao.append(construcao)
        self.grid_mapa[construcao.x][construcao.y] = construcao
        self.model.grid.place_agent(self, (construcao.x , construcao.y))

    def is_posicao_vazia(self: AgenteMapa, x: int, y: int) -> bool:
        if not isinstance(self.grid_mapa[x][y], Objeto):
            return True
        return False
    
    def is_posicao(self: AgenteMapa, x: int, y: int) -> bool:
        if x < len(self.grid_mapa) and x >= 0 and y < len(self.grid_mapa[0]) and y >= 0:
            return True
        return False   
