from agent.agente_coletor import AgenteColetor
from agent.agente_construtor import AgenteConstrutor
from agent.agente_mapa import AgenteMapa
from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.UserParam import StaticText
from agent.modelo_agente import ModeloAgente
from model.natural.pedra import Pedra
from model.natural.arvore import Arvore
from model.construcao.casa import Casa
from model.construcao.predio import Predio

def recursos(modelo):
    if type(modelo) is ModeloAgente:
        madeira, pedra = modelo.get_total_recursos()
        return (f'Total de madeiras coletadas: {madeira}; Total de pedras coletadas: {pedra}')
    else:
        return f""

def agentPortrayal(agent):
    portrayal = {"Filled": "true",
                "r": 0.5}
    if type(agent) is AgenteColetor: 
        portrayal['Shape'] = "assets/coletor.png"
        portrayal['Layer'] = 2
    elif type(agent) is AgenteConstrutor:
        portrayal['Shape'] = "assets/construtor.png"
        portrayal['Layer'] = 2
    elif type(agent) is AgenteMapa:
        portrayal['Shape'] = "assets/mapa.png"
    elif type(agent) is Pedra:
        portrayal['Shape'] = 'assets/pedra.png'
        portrayal['Valor'] = agent.valor
        portrayal['Layer'] = 2
    elif type(agent) is Arvore:
        portrayal['Shape'] = 'assets/madeira.png'
        portrayal['Valor'] = agent.valor
        portrayal['Layer'] = 2
    elif type(agent) is Casa:
        portrayal['Shape'] = 'assets/casa.png'
        portrayal['Layer'] = 1
    elif type(agent) is Predio:
        portrayal['Shape'] = 'assets/predio.png'
        portrayal['Layer'] = 0
    return portrayal

canvas_element = CanvasGrid(agentPortrayal, 10, 10, 500, 500)

server =  ModularServer(
    ModeloAgente, [canvas_element, recursos], "Pseudo RTS"
)

server.port = 8521

