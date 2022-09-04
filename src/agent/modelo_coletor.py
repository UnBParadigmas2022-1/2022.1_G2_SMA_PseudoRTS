from mesa import Model
import mesa

from agent.agente_coletor import AgenteColetor
from agent.agente_mapa import AgenteMapa
from utils.utils import posicao_aleatoria
from mesa.space import MultiGrid



class ModeloColetor(Model):
    def __init__(self, num_agentes: int, mapa: AgenteMapa) -> None:
        self.num_agentes = num_agentes
        self.mapa = mapa
        self.grid = MultiGrid(10,10, True)
        self.schedule = mesa.time.RandomActivation(self)

        for i in range(1, num_agentes + 1):
            agente = AgenteColetor(i, self, posicao_aleatoria(), posicao_aleatoria())
            self.schedule.add(agente)

    def step(self) -> None:
        return self.schedule.step()