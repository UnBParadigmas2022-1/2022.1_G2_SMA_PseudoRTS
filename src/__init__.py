from model.natural.arvore import Arvore
from model.construcao.casa import Casa

def run() -> None:
    arvore = Arvore()
    print("arvore = " + str(arvore.valor))
    casa = Casa()
    print("casa = " + str(casa.valor_pedra))

if __name__ == '__main__':
    run()
