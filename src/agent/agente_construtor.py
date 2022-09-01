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
    """
    todo:
    protocolo de comunicacao
    perguntar para o agente coletor se tem item
    se sim construir com base na quantidade 
    se nao ir coletar
    enviar sempre ao mapa a localizacao
    pergunto ao mapa quem é coletor 
    - tiago é coletor
        - tiago, vc tem pedra e madeira  <<---
            - responder tenho x e y
                - Quero w e t 
                    - enviar w e t 
                        - construir
                            - vai se mover e mandar a informação pro mapa
                                - construir onde n tem Objeto
                    - Não existe ou demorou muito para responder
            - Não existe ou demorou muito para responder
    - Não existe ou demorou muito para responder
    - vai coletar
    """

    place_holder_predio = Predio()
    place_holder_casa = Casa()
    def __init__(self: AgenteConstrutor, unique_id: int, model: "Model", x: int = 0, y: int = 0) -> None:
        super(AgenteConstrutor, self).__init__(unique_id, model, x, y)
        self.is_construindo = False
        self.local_vazio = {"x": 0, "y": 0} # perguntar para o mapa isso

    def step(self: AgenteConstrutor) -> None: 
        if (self.is_construindo):
            self.constroi()
        elif not isinstance(self.material_construcao(), type(None)):
            self.anda_local_vazio()
        else:
            self.comportamento_coletor()

    def comportamento_coletor(self: AgenteConstrutor) -> None:
        if (self.is_coletando):
            self.coleta()
        elif (self.recurso != None):
            self.anda()
        else:
            self.define_recurso()

    def compara_distancia_para_vazio(self, pos: posicao):
        return sqrt((self.x - pos.x)**2+(self.y - pos.y)**2)
    
    def anda_local_vazio(self: AgenteConstrutor) -> None:
        if (self.x < self.local_vazio['x']):
            self.x += 1
        elif (self.y < self.local_vazio['y']):
            self.y += 1
        elif (self.y > self.local_vazio['y']):
            self.y -= 1
        elif (self.x > self.local_vazio['x']):
            self.x -= 1
        # enviar para o mapa nova posicao
        if (self.local_vazio['x'] == self.x and self.local_vazio['y'] == self.y):
            self.is_construindo = True

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
        
        print(f'CONSTRUINDO! {type(self.construcao)}. Posição atual [{self.x}, {self.y}]')
        self.is_construindo = False
        self.quantidade_madeira = self.quantidade_madeira - self.construcao.valor_madeira
        self.quantidade_pedra = self.quantidade_pedra - self.construcao.valor_pedra
        print(f'Recurso utilizado:')
        print(f'Quantidade de madeira atual: {self.quantidade_madeira}')
        print(f'Quantidade de pedra atual: {self.quantidade_pedra}')
        self.construcao = None
        
