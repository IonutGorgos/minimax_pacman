class Pacman:
    def __init__(self):
        self.score = 0
        self.start = (7, 6)
        self.dx = None
        self.dy = None

    def getScore(self):
        return self.score