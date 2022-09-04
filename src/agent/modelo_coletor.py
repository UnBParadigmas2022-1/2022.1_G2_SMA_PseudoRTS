from mesa import Model
import mesa

from agent.agente_coletor import AgenteColetor
from utils.utils import posicao_aleatoria


class ModeloColetor(Model):
    def __init__(self, num_agentes: int, recursos: list) -> None:
        self.num_agentes = num_agentes
        self.recursos = recursos
        self.schedule = mesa.time.RandomActivation(self)

        for i in range(1, num_agentes + 1):
            agente = AgenteColetor(i, self, posicao_aleatoria(), posicao_aleatoria())
            self.schedule.add(agente)

    def step(self) -> None:
        return self.schedule.step()