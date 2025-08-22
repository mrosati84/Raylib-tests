from entities.entity import Entity
from util.next_step import next_step


class Move:
    def __init__(self, destination: tuple):
        self.destination = destination

    def operate(self, agent: Entity):
        # print(
        #     f"Agente {agent.entity_id} opero task move. Destinazione: {self.destination}, posizione attuale: {agent.pos}"
        # )
        print(f"{agent.pos}")
        agent.pos = tuple(next_step(agent.pos, self.destination))
