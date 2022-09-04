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

    def step(self: AgenteColetor) -> None:
        if (self.is_coletando):
            self.coleta()
        elif (self.recurso != None):
            self.anda()
        else:
            self.define_recurso()

    def coleta(self: AgenteColetor) -> None:
        if self.recurso in self.model.mapa.get_recursos():
            if (isinstance(self.recurso, Pedra)):
                self.quantidade_pedra += self.recurso.valor
            elif (isinstance(self.recurso, Arvore)):
                self.quantidade_madeira += self.recurso.valor
            print(f'Agente {self.unique_id} Recurso coletado:')
            print(f'Agente {self.unique_id} Quantidade de madeira atual: {self.quantidade_madeira}')
            print(f'Agente {self.unique_id} Quantidade de pedra atual: {self.quantidade_pedra}')
            self.model.mapa.remove_recursos(self.recurso)
            
        else:
            print(f'Agente {self.unique_id} Roubaram meu recurso!')
        self.recurso = None
        self.is_coletando = False


    def anda(self: AgenteColetor) -> None:
        print(f'Agente {self.unique_id} ANDANDO! Posição atual [{self.x}, {self.y}]')
        if (self.x < self.recurso.x):
            self.x += 1
        elif (self.y < self.recurso.y):
            self.y += 1
        elif (self.y > self.recurso.y):
            self.y -= 1
        elif (self.x > self.recurso.x):
            self.x -= 1
        if (self.recurso.x == self.x and self.recurso.y == self.y):
            self.is_coletando = True

    def define_recurso(self: AgenteColetor) -> None:
        if (len(self.model.mapa.get_recursos()) > 0):
            self.recurso = min(self.model.mapa.get_recursos(), key=self.compara_distancia_para_recurso)
            print(f'Agente {self.unique_id} Posição do recurso [{self.recurso.x}, {self.recurso.y}]')

    def get_material(self: AgenteColetor) -> [int, int]:
        return self.quantidade_madeira, self.quantidade_pedra

    def coleta_material(self: AgenteColetor) ->[ int, int]:
        self.quantidade_madeira = 0
        self.quantidade_pedra = 0
        return self.quantidade_madeira, self.quantidade_pedra
