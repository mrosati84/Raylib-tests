import random
from util.random_name import random_name


class NPC:
    def __init__(self):
        self.name: str = random_name()
        self.piloting: int = random.randint(0, 100)
        self.management: int = random.randint(0, 100)
        self.ethics: int = random.randint(0, 100)
