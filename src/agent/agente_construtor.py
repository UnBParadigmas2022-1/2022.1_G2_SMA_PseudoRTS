from __future__ import annotations
from typing import Dict, Any
from .agente_coletor import AgenteColetor
from mesa import Model
from math import sqrt

from model.construcao.construcao import Construcao
from model.construcao.casa import Casa
from model.construcao.predio import Predio

posicao = Dict[str, Any]

class AgenteConstrutor(AgenteColetor):
    place_holder_predio = Predio()
    place_holder_casa = Casa()
    def __init__(self: AgenteConstrutor, unique_id: int, model: "Model", x: int = 0, y: int = 0) -> None:
        super(AgenteConstrutor, self).__init__(unique_id, model, x, y)
        self.is_construindo = False

    def step(self: AgenteConstrutor) -> None: 
        if (self.is_construindo):
            self.constroi()
        elif not isinstance(self.material_construcao(), type(None)):
            self.anda_local_vazio(1)
        else:
            self.comportamento_coletor()

    def comportamento_coletor(self: AgenteConstrutor) -> None:
        if (self.is_coletando):
            self.coleta()
        elif (self.recurso != None):
            self.anda()
        else:
            self.define_recurso()

    def anda_local_vazio(self: AgenteConstrutor, soma: int) -> None:
        if self.model.mapa.is_posicao_vazia(self.x, self.y):
            self.is_construindo = True

        if self.model.mapa.is_posicao(self.x + soma, self.y):
            self.x += soma
        elif self.model.mapa.is_posicao(self.x, self.y + soma):
            self.y += soma
        elif self.model.mapa.is_posicao(self.x - soma, self.y):
            self.x -= soma
        elif self.model.mapa.is_posicao(self.x, self.y - soma):
            self.y -= soma
        elif self.model.mapa.is_posicao(self.x - soma, self.y - soma):
            self.x -= soma
            self.y -= soma
        elif self.model.mapa.is_posicao(self.x + soma, self.y + soma):
            self.x += soma
            self.y += soma
        else: 
            self.anda_local_vazio(soma + 1)
        self.model.grid.move_agent(self, (self.x, self.y))

        if soma >= 4:
            print(f'Agente {self.unique_id} Você esta sem local!')

    def material_construcao(self: AgenteConstrutor) -> type:
        if self.quantidade_madeira >= self.place_holder_predio.valor_madeira:
            if self.quantidade_pedra >= self.place_holder_predio.valor_pedra:
                return Predio
        elif self.quantidade_madeira >= self.place_holder_casa.valor_madeira:
            if self.quantidade_pedra >= self.place_holder_casa.valor_pedra:
                return Casa
        return None

    def constroi(self: AgenteConstrutor) -> None:
        tipo = self.material_construcao()
        if tipo == Predio:
            self.construcao = Predio(self.x, self.y)
        elif tipo == Casa:
            self.construcao = Casa(self.x, self.y)
        
        print(f'Agente {self.unique_id} CONSTRUINDO! {type(self.construcao)}. Posição atual [{self.x}, {self.y}]')
        self.model.mapa.set_construcao(self.construcao)
        self.is_construindo = False
        self.quantidade_madeira = self.quantidade_madeira - self.construcao.valor_madeira
        self.quantidade_pedra = self.quantidade_pedra - self.construcao.valor_pedra
        print(f'Agente {self.unique_id} Recurso utilizado:')
        print(f'Agente {self.unique_id} Quantidade de madeira atual: {self.quantidade_madeira}')
        print(f'Agente {self.unique_id} Quantidade de pedra atual: {self.quantidade_pedra}')
        self.construcao = None
        