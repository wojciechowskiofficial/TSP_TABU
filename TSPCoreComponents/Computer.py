import math

class Computer:
    def dist(first: list, second: list):
        return math.sqrt((second[0] - first[0]) ** 2 + (second[1] - first[1]) ** 2)

    def minDist(currPos, vertices: list):
        minIndex = 0
        minDist = Computer.dist(currPos, vertices[0].getPos())
        for i in range(len(vertices)):
            if Computer.dist(currPos, vertices[i].getPos()) < minDist:
                minDist = Computer.dist(currPos, vertices[i].getPos())
                minIndex = i

        return {'minIndex': minIndex, 'minDist': minDist}