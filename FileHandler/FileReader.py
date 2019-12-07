import os
from TSPCoreComponents.Vertex import Vertex

class FileReader:
    def __init__(self, fileName):
        self.fileName = fileName
        self.createPath()
        self.instance = list()

    def createPath(self):
        if not os.path.exists('IOFiles'):
            os.makedirs('IOFiles')
        self.filePath = 'IOFiles/' + self.fileName


    def importInstance(self):
        with open(self.filePath, 'r') as f:
            instanceSize = int(next(f))

            def readPos():
                tmpString = f.readline().split()
                return [int(tmpString[1]), int(tmpString[2])]

            for i in range(instanceSize):
                tmpVertex = Vertex()
                tmpVertex.setPos(readPos())
                tmpVertex.id = i
                self.instance.append(tmpVertex)

        return self.instance
