from agent.agente_coletor import AgenteColetor
from agent.agente_construtor import AgenteConstrutor
from agent.agente_mapa import AgenteMapa
from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.UserParam import UserSettableParameter
from agent.modelo_agente import ModeloAgente
from model.natural.pedra import Pedra
from model.natural.arvore import Arvore
from model.construcao.casa import Casa
from model.construcao.predio import Predio


def agentPortrayal(agent):
    portrayal = {"Filled": "true",
                "Layer": 0,
                "Color": "red",
                "r": 0.5}
    if type(agent) is AgenteColetor: 
        portrayal['Shape'] = "assets/coletor.png"
    elif type(agent) is AgenteConstrutor:
        portrayal['Shape'] = "assets/construtor.png"
    elif type(agent) is AgenteMapa:
        portrayal['Shape'] = "assets/mapa.png"
    elif type(agent) is Pedra:
        portrayal['Shape'] = 'assets/pedra.png'
    elif type(agent) is Arvore:
        portrayal['Shape'] = 'assets/madeira.png'
    elif type(agent) is Casa:
        portrayal['Shape'] = 'assets/casa.png'
    elif type(agent) is Predio:
        portrayal['Shape'] = 'assets/predio.png'
    return portrayal

canvas_element = CanvasGrid(agentPortrayal, 10, 10, 500, 500)

server =  ModularServer(
    ModeloAgente, [canvas_element]
)

server.port = 8521

