from mesa import Model
import mesa

from agent.agente_coletor import AgenteColetor
from agent.agente_construtor import AgenteConstrutor
from model.mapa import Mapa
from utils.utils import posicao_aleatoria

class ModeloAgente(Model):
    def __init__(self, mapa: Mapa, num_agentes_coletor: int = 2, num_agentes_construtor: int = 2) -> None:
        self.num_agentes_coletor = num_agentes_coletor
        self.num_agentes_construtor = num_agentes_construtor
        self.mapa = mapa
        self.schedule = mesa.time.RandomActivation(self)

        for i in range(1, num_agentes_coletor + 1):
            agente_coletor = AgenteColetor(i, self, posicao_aleatoria(), posicao_aleatoria())
            self.schedule.add(agente_coletor)
        
        for i in range(num_agentes_coletor + 1, num_agentes_coletor + num_agentes_construtor + 1):
            agente_construtor = AgenteConstrutor(i, self, posicao_aleatoria(), posicao_aleatoria())
            self.schedule.add(agente_construtor)

    def step(self) -> None:
        return self.schedule.step()
