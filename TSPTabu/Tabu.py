from TSPGreedy.Greedy import Greedy
from TSPTabu.TabuMatrix import TabuMatrix
from TSPTabu.PowerSet import PowerSet

class Tabu:
    #Tabu class constructor takes instance parameters as arguments
    #maxIter: maximal number of main for loop iterations
    #uIter: maximal number of iterations during which objective function value does not change by uValue
    #uValue: value that objective function value should decrease by during uIter iterations
    #aspiration: value which swaping a banned pair of vertices should decrease the objective function value by
    #to ignore the fact that the pair is currently in tabu matrix
    def __init__(self, inputVector, **kwargs):
        self.maxIter = kwargs['maxIter']
        self.uIter = kwargs['uIter']
        self.uValue = kwargs['uValue']
        self.aspiration = kwargs['aspiration']
        self.inputVector = inputVector

    def solveTabu(self):
        self.initialize()
        #                                           $$$$IMPORTANT$$$$
        #CONVENTION: from the moment of self.initialInstance being generated self.solution contains two instances
        #of the first vertex (as 0th and last element of list). this implies that the length of self.solution
        #is greater than actual solution vector with unique only vertices by exactly 1.
        self.powerset = PowerSet(self.solution)

    def initialize(self):
        self.initialInstance = Greedy(self.inputVector)
        self.initialInstance.solveGreedy()
        self.solution = self.initialInstance.solution
        self.tabuMatrix = TabuMatrix(len(self.solution) - 1)
