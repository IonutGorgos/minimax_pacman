import random


class Ghost:
    def __init__(self):
        self.score = 0
        self.dx = None
        self.dy = None
        self.movex = 0
        self.movey = 0

    def move(self):
        # move in random directions.

        self.movex = random.randint(-1, 1)
        self.movey = random.randint(-1, 1)
        self.dx += self.movex
        self.dy += self.movey
