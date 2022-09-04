from mesa import Model
import mesa

from agent.agente_coletor import AgenteColetor
from agent.agente_construtor import AgenteConstrutor
from agent.agente_mapa import AgenteMapa
from utils.utils import genPos
from mesa.space import MultiGrid


class ModeloAgente(Model):
    def __init__(self, num_agentes_coletor: int = 1, num_agentes_construtor: int = 2) -> None:
        self.num_agentes_coletor = num_agentes_coletor
        self.num_agentes_construtor = num_agentes_construtor

        self.schedule = mesa.time.RandomActivation(self)
        self.grid = MultiGrid(10,10, True)
        self.running = True
        self.filledPositions = []

        self.mapa = AgenteMapa(0, self, 10, 10)
        self.mapa.preenche_mapa(5)

        for i in range(1, num_agentes_coletor + 1):
            x, y = genPos()
            while (x,y) in self.filledPositions:
                x, y = genPos()
            self.filledPositions.append((x,y))
            agente = AgenteColetor(i, self, x, y)
            self.schedule.add(agente)
            self.grid.place_agent(agente, (x , y))
        
        for i in range(num_agentes_coletor + 1, num_agentes_coletor + num_agentes_construtor + 1):
            x, y = genPos()
            while (x,y) in self.filledPositions:
                x, y = genPos()
            self.filledPositions.append((x,y))
            agente = AgenteConstrutor(i, self, x, y)
            self.schedule.add(agente)
            self.grid.place_agent(agente, (x , y))

    def step(self) -> None:
        return self.schedule.step()

    def get_material_coletor(self):
        madeira_final = 0
        pedra_final = 0
        for agente in self.schedule.agent_buffer():
            if isinstance(agente, AgenteColetor) and not isinstance(agente, AgenteConstrutor):
                madeira, pedra = agente.coleta_material()
                madeira_final += madeira
                pedra_final += pedra
        return madeira_final, pedra_final
