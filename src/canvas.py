from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.UserParam import UserSettableParameter
from agent.modelo_coletor import ModeloColetor
from agent.agente_mapa import AgenteMapa

def agentPortrayal(agent):
    portrayal = {"Shape": "circle",
                 "Filled": "true",
                 "Layer": 0,
                 "Color": "red",
                 "r": 0.5}
    return portrayal

canvas_element = CanvasGrid(agentPortrayal, 10, 10, 500, 500)

mapa = AgenteMapa(11, 11)
mapa.preenche_mapa(10)

server =  ModularServer(
    ModeloColetor, [canvas_element], "Mapa", {"num_agentes":1, "mapa":mapa}
)

server.port = 8521
