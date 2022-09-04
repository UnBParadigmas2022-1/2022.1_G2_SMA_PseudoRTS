from model.natural.arvore import Arvore
from model.construcao.casa import Casa
from agent.modelo_coletor import ModeloColetor
from model.natural.pedra import Pedra

def run() -> None:
    arvore = Arvore(5, 5)
    pedra = Pedra(3, 3)
    print("arvore = " + str(arvore.valor))
    casa = Casa(2, 3)
    print("casa = " + str(casa.valor_pedra))
    modelo_coletor = ModeloColetor(1, [arvore, pedra])
    for i in range(20):
        modelo_coletor.step()

if __name__ == '__main__':
    run()
