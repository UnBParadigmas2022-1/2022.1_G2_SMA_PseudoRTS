from agent.modelo_agente import ModeloAgente
from model.mapa import Mapa

def run() -> None:
    mapa = Mapa(11, 11)
    mapa.preenche_mapa(10)
    modelo_agente = ModeloAgente(mapa, 1, 1)
    for i in range(100000):
        modelo_agente.step()

if __name__ == '__main__':
    run()
