from agent.modelo_coletor import ModeloColetor
from agent.agente_mapa import AgenteMapa
from canvas import server


def run() -> None:
    mapa = AgenteMapa(11, 11)
    mapa.preenche_mapa(10)
    modelo_coletor = ModeloColetor(1, mapa)
    for i in range(20):
        modelo_coletor.step()
    

if __name__ == '__main__':
    server.launch()