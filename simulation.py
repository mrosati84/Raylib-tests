from typing import List
from entities.operable_entity import OperableEntity


class Simulation:
    def __init__(self):
        self.agents: List[OperableEntity] = []

    def tick(self):
        for agent in self.agents:
            if agent.tasks:
                task = agent.tasks[0]
                task.operate(agent)

    def add_agent(self, agent: OperableEntity):
        self.agents.append(agent)
