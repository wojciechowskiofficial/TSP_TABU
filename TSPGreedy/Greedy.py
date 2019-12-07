from TSPCoreComponents.SolutionContainer import SolutionContainer
from TSPCoreComponents.Computer import Computer

class Greedy:
    def __init__(self, inputVector):
        self.inputVector = inputVector
        self.initialSize = len(self.inputVector)

    def solveGreedy(self):
        self.solution = SolutionContainer()
        self.solution.verticesVector.append(self.inputVector[0])
        tmp = self.inputVector[0]
        del self.inputVector[0]
        for i in range(self.initialSize - 1):
            tmpComputation = Computer.minDist(tmp.getPos(), self.inputVector)
            self.solution.verticesVector.append(self.inputVector[tmpComputation['minIndex']])
            self.solution.objFunctValue += tmpComputation['minDist']
            tmp = self.inputVector[tmpComputation['minIndex']]
            del self.inputVector[tmpComputation['minIndex']]

        """
            merging last vertex from self.solution.vertices with first vertex considered
            to create a 'physical cycle' of vertices.
        """

        self.solution.verticesVector.append(self.solution.verticesVector[0])
        self.solution.objFunctValue += Computer.dist(self.solution.verticesVector[0].getPos(), tmp.getPos())
