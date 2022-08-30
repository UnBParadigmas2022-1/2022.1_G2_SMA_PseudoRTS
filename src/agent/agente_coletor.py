from __future__ import annotations
from model.objeto import Objeto
from mesa import Agent, Model

class AgenteColetor(Agent, Objeto):

    def __init__(self: AgenteColetor, unique_id: int, model: "Model", x: int = 0, y: int = 0) -> None:
        Agent.super(AgenteColetor, self).__init__(unique_id, model)
        Objeto.super(AgenteColetor, self).__init__(x, y)
