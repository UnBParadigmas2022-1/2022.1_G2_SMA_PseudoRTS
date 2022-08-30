from __future__ import annotations
from .agente_coletor import AgenteColetor
from mesa import Model

class AgenteConstrutor(AgenteColetor):
    """
    todo:
    protocolo de comunicacao
    perguntar para o agente coletor se tem item
    se sim construir com base na quantidade 
    se nao ir coletar
    enviar sempre ao mapa a localizacao
    """

    def __init__(self: AgenteConstrutor, unique_id: int, model: "Model", x: int = 0, y: int = 0) -> None:
        super(AgenteConstrutor, self).__init__(unique_id, model, x, y)

    
