from model.natural.arvore import Arvore
from model.construcao.casa import Casa
from agent.modelo_coletor import ModeloColetor
from agent.modelo_construtor import ModeloConstrutor
from model.natural.pedra import Pedra

def run() -> None:
    modelo_construtor = ModeloConstrutor(1, [Arvore(5, 5), Arvore(3, 5), Pedra(2, 3), Pedra(1, 3)])
    for i in range(20):
        modelo_construtor.step()

if __name__ == '__main__':
    run()
