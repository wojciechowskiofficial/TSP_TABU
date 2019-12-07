from TSPGreedy.Greedy import Greedy
from TSPTabu.TabuMatrix import TabuMatrix

class Tabu:
    #Tabu class constructor takes instance parameters as arguments
    #maxIter: maximal number of main for loop iterations
    #uIter: maximal number of iterations during which objective function value does not change by uValue
    #uValue: value that objective function value should decrease by during uIter iterations
    #aspiration: value which swaping a banned pair of vertecies should decrease the objective function value by
    #to ignore the fact that the pair is currently in tabu matrix
    def __init__(self, inputVector, maxIter, uIter, uValue, aspiration):
        self.maxIter = maxIter
        self.aspiration = aspiration
        self.inputVector = inputVector
        self.initialSize = len(self.inputVector)

    def solveTabu(self):
        self.initialInstance = Greedy(self.inputVector)
        self.initialInstance.solveGreedy()
        self.solution = self.initialInstance.solution
