from mesa import Model
from mesa.time import RandomActivation

from agent.agente_construtor import AgenteConstrutor
from utils.utils import posicao_aleatoria

class ModeloConstrutor(Model):
    def __init__(self, num_agentes: int, recursos: list) -> None:
        self.num_agentes = num_agentes
        self.recursos = recursos
        self.running = True
        self.schedule = RandomActivation(self)

        for i in range(self.num_agentes):
            agente = AgenteConstrutor(i, self, posicao_aleatoria(), posicao_aleatoria())
            self.schedule.add(agente)

    def step(self) -> None:
        return self.schedule.step()
