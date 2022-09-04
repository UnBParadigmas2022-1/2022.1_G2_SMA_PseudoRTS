from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.UserParam import UserSettableParameter
from agent.modelo_agente import ModeloAgente
from model.mapa import Mapa


def agentPortrayal(agent):
    portrayal = {"Shape": "assets/coletor.png",
                 "Filled": "true",
                 "Layer": 0,
                 "Color": "red",
                 "r": 0.5}
    return portrayal

canvas_element = CanvasGrid(agentPortrayal, 10, 10, 500, 500)

mapa = Mapa(11, 11)
mapa.preenche_mapa(10)

server =  ModularServer(
    ModeloAgente, [canvas_element], "Mapa", {"mapa":mapa}
)

server.port = 8521

