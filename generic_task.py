from typing import Literal
from tasks.move import Move
from tasks.load import Load


class Task:
    def __init__(self, task_type: Literal["MOVE", "LOAD"], **kwargs):
        self.task_type = task_type

        if self.task_type == "MOVE":
            self.task_class = Move(kwargs.get("destination"))
        if self.task_type == "LOAD":
            self.task_class = Load(kwargs.get("cargo"))

    def operate(self, agent):
        self.task_class.operate(agent)
