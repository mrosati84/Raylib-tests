from typing import List
from entities.operable_entity import OperableEntity
from generic_task import Task


class Station(OperableEntity):
    def __init__(self, entity_id: int, pos: tuple, cargo, tasks: List[Task]):
        super().__init__(entity_id, pos, tasks)
        self.cargo = cargo
