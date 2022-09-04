from __future__ import annotations
from math import sqrt
from model.objeto import Objeto
from mesa import Agent, Model

from model.natural.natural import Natural
from model.natural.pedra import Pedra
from model.natural.arvore import Arvore

class AgenteColetor(Objeto, Agent):
    recurso: Natural

    def __init__(self: AgenteColetor, unique_id: int, model: "Model", x: int = 0, y: int = 0) -> None:
        self.unique_id = unique_id
        self.model = model
        super().__init__(x, y)
        self.recurso = None
        self.is_coletando = False
        self.quantidade_madeira = 0
        self.quantidade_pedra = 0

    def compara_distancia_para_recurso(self, recurso: Natural):
        return sqrt((self.x - recurso.x)**2+(self.y - recurso.y)**2)

    def step(self) -> None:
        if (self.is_coletando):
            self.coleta()
        elif (self.recurso != None):
            self.anda()
        else:
            self.define_recurso()

    def coleta(self) -> None:
        if (isinstance(self.recurso, Pedra)):
            self.quantidade_pedra += self.recurso.valor
        elif (isinstance(self.recurso, Arvore)):
            self.quantidade_madeira += self.recurso.valor
        self.model.mapa.get_recursos().remove(self.recurso)
        self.recurso = None
        self.is_coletando = False
        print(f'Recurso coletado:')
        print(f'Quantidade de madeira atual: {self.quantidade_madeira}')
        print(f'Quantidade de pedra atual: {self.quantidade_pedra}')


    def anda(self):
        print(f'ANDANDO! Posição atual [{self.x}, {self.y}]')
        if (self.x < self.recurso.x):
            self.x += 1
        elif (self.y < self.recurso.y):
            self.y += 1
        elif (self.y > self.recurso.y):
            self.y -= 1
        elif (self.x > self.recurso.x):
            self.x -= 1
        self.model.grid.move_agent(self, (self.x, self.y))

        if (self.recurso.x == self.x and self.recurso.y == self.y):
            self.is_coletando = True

    def define_recurso(self):
        if (len(self.model.mapa.get_recursos()) > 0):
            self.recurso = min(self.model.mapa.get_recursos(), key=self.compara_distancia_para_recurso)
            print(f'Posição do recurso [{self.recurso.x}, {self.recurso.y}]')
