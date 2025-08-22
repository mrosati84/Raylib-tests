from typing import List
from generic_task import Task
from entities.operable_entity import OperableEntity


class Ship(OperableEntity):
    def __init__(self, entity_id: int, pos: tuple, cargo: int, tasks: List[Task]):
        super().__init__(entity_id, pos, tasks)
        self.cargo = cargo
