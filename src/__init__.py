from agent.modelo_coletor import ModeloColetor
from agent.modelo_construtor import ModeloConstrutor
from agent.agente_mapa import AgenteMapa

def run() -> None:
    mapa = AgenteMapa(11, 11)
    mapa.preenche_mapa(10)
    modelo_coletor = ModeloColetor(1, mapa)
    modelo_construtor = ModeloConstrutor(1, mapa)
    for i in range(20):
        modelo_construtor.step()

if __name__ == '__main__':
    run()
