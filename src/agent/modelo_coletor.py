from mesa import Model
import mesa

from agent.agente_coletor import AgenteColetor
from agent.agente_mapa import AgenteMapa
from utils.utils import posicao_aleatoria
from random import randrange
from mesa.space import MultiGrid

def genPos():
    x = randrange(10)
    y = randrange(10)
    return x, y

class ModeloColetor(Model):
    def __init__(self, num_agentes: int, mapa: AgenteMapa) -> None:
        self.num_agentes = num_agentes
        self.mapa = mapa
        self.schedule = mesa.time.RandomActivation(self)
        self.grid = MultiGrid(10,10, True)
        self.running = True
        self.filledPositions = []

        for i in range(1, num_agentes + 1):
            x, y = genPos()
            while (x,y) in self.filledPositions:
                x, y = genPos()
            self.filledPositions.append((x,y))
            agente = AgenteColetor(i, self, posicao_aleatoria(), posicao_aleatoria())
            self.schedule.add(agente)
            self.grid.place_agent(agente, (x , y))

    def step(self) -> None:
        return self.schedule.step()
