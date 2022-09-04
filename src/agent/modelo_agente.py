from mesa import Model
import mesa

from agent.agente_coletor import AgenteColetor
from agent.agente_construtor import AgenteConstrutor
from model.mapa import Mapa
from utils.utils import posicao_aleatoria
from random import randrange
from mesa.space import MultiGrid

def genPos():
    x = randrange(10)
    y = randrange(10)
    return x, y

class ModeloAgente(Model):
    def __init__(self, mapa: Mapa, num_agentes_coletor: int = 2, num_agentes_construtor: int = 2) -> None:
        self.num_agentes_coletor = num_agentes_coletor
        self.num_agentes_construtor = num_agentes_construtor
        self.mapa = mapa
        self.schedule = mesa.time.RandomActivation(self)
        self.grid = MultiGrid(10,10, True)
        self.running = True
        self.filledPositions = []

        for i in range(1, num_agentes_coletor + 1):
            x, y = genPos()
            while (x,y) in self.filledPositions:
                x, y = genPos()
            self.filledPositions.append((x,y))
            agente = AgenteColetor(i, self, posicao_aleatoria(), posicao_aleatoria())
            self.schedule.add(agente)
            self.grid.place_agent(agente, (x , y))
        
        for i in range(num_agentes_coletor + 1, num_agentes_coletor + num_agentes_construtor + 1):
            x, y = genPos()
            while (x,y) in self.filledPositions:
                x, y = genPos()
            self.filledPositions.append((x,y))
            agente = AgenteConstrutor(i, self, posicao_aleatoria(), posicao_aleatoria())
            self.schedule.add(agente)
            self.grid.place_agent(agente, (x , y))

    def step(self) -> None:
        return self.schedule.step()
