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

    def overVec(vec: list()):
        acc = 0
        #already contains full cycle with connected first/last vertex
        for i in range(1, len(vec)):
            first = vec[i - 1].getPos()
            second = vec[i].getPos()
            acc += Computer.dist(first, second)
        return acc