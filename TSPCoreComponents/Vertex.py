class Vertex:
    def __init__(self):
        self.x = float()
        self.y = float()
        self.id = int()

    def __str__(self):
        return '[id: ' + str(self.id) + ' x: ' + str(self.x) + ' y: ' + str(self.y) + ']'

    def __repr__(self):
        return self.__str__()

    def getPos(self):
        return [self.x, self.y]

    def setPos(self, posList: list):
        self.x = posList[0]
        self.y = posList[1]

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y
