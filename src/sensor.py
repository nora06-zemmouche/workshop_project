import random


class Sensor:
    def __init__(self, name="Sensor"):
        self.name = name

    def read(self):
        # Simule une lecture aléatoire
        return random.randint(0, 100)
