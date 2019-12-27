from TSPGreedy.Greedy import Greedy
from TSPTabu.TabuMatrix import TabuMatrix
from TSPTabu.PowerSet import PowerSet
from TSPTabu.SwapPair import SwapPair
from copy import deepcopy

class Tabu:
    #Tabu class constructor takes instance parameters as arguments
    #maxIter: maximal number of main for loop iterations
    #uIter: maximal number of iterations during which objective function value does not change by uValue
    #uValue: value that objective function value should decrease by during uIter iterations
    #aspiration: value which swaping a banned pair of vertices should decrease the objective function value by
    #to ignore the fact that the pair is currently in tabu matrix
    #banPeriod: number of iterations during which banned pair stays in tabu matrix
    def __init__(self, inputVector, **kwargs):
        self.maxIter = kwargs['maxIter']
        self.uIter = kwargs['uIter']
        self.uValue = kwargs['uValue']
        self.aspiration = kwargs['aspiration']
        self.banPeriod = kwargs['banPeriod']
        self.inputVector = inputVector


    def solveTabu(self):
        self.initialize()
        #                                           $$$$IMPORTANT$$$$
        #CONVENTION: from the moment of self.initialInstance being generated self.solution contains two instances
        #of the first vertex (as 0th and last element of list). this implies that the length of self.solution
        #is greater than actual solution vector with unique only vertices by exactly 1.

        #if maxIter paramter specified
        if self.maxIter is not None:
            self.numberOfIterations = 0

        for i in range(100):
            #decrement tabu values
            self.tabuMatrix.decrement()
            # generate powerset of feasible solutions
            self.powerset = PowerSet(self.solution)
            # chose next solution taking tabu matrix and aspiration under consideration
            self.nextPair = self.choseNext()
            # tag newly chosen solution as tabu
            self.tabuMatrix.set(self.nextPair.first, self.nextPair.second, self.banPeriod)
            # assing self.solution <- self.nextPair as 'transition' step in main algo. loop
            self.solution = self.nextPair.vec
            # check if self.solution is globally optimal and substitute if True
            if self.solution.objFunctValue < self.globallyOptimal.objFunctValue:
                self.globallyOptimal = self.solution
            #if maxIter paramter specified
            if self.maxIter is not None:
                self.numberOfIterations += 1
                if self.numberOfIterations == self.maxIter:
                    break


    def initialize(self):
        self.initialInstance = Greedy(self.inputVector)
        self.initialInstance.solveGreedy()
        self.solution = self.initialInstance.solution
        self.greedySolution = deepcopy(self.solution)
        self.tabuMatrix = TabuMatrix(len(self.solution) - 1)
        #initialize globally optimal solution with initial greedy solution
        self.globallyOptimal = deepcopy(self.solution)

    def isTabu(self, vec):
        if self.tabuMatrix.get(vec.first, vec.second) == 0:
            return False
        else:
            return True

    #this method shall be performed on SolutionContainer that is already in TabuMatrix
    #condition of aspiration: >=
    def isAspiring(self, vec: SwapPair):
        if abs(self.solution.objFunctValue - vec.objFunctValue) >= self.aspiration:
            return True
        else:
            return False

    def choseNext(self):
        tmp = None
        for tmp in self.powerset.pairs:
            if self.isTabu(tmp):
                if self.isAspiring(tmp):
                    return tmp
            else:
                return tmp
        if tmp is None:
            print('no feasible solution found')
            exit(0)
