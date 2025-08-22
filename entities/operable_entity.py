from typing import List
from generic_task import Task
from entities.entity import Entity


class OperableEntity(Entity):
    def __init__(self, entity_id: int, pos: tuple, tasks):
        super().__init__(entity_id, pos)
        self.tasks: List[Task] = tasks
