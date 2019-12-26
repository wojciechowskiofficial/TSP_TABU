"""
this class is ment to be complex data type used to generate and store
power set of pairs that are potentially to be swapped. this set DOES NOT
contain pairs such (sameValue; sameValue). instances of this class
should be deleted after each iteration of TSPTabu main for loop.
"""

from copy import deepcopy
from TSPTabu.SwapPair import SwapPair

class PowerSet:
    def __init__(self, vec: list()):
        self.vec = deepcopy(vec)
        self.pairs = list()
        self.genAllPairs()
        self.pairs.sort(key = lambda x : x.objFunctValue)

    #cardinality of self.pairs is going to be C(len(self.vec) - 2, 2)
    #since first and last element of self.vec is duplicate of each other
    #and by assumption should be fixed in place
    def genAllPairs(self):
        for i in range(1, len(self.vec) - 1):
            for j in range(i + 1, len(self.vec) - 1):
                self.pairs.append(SwapPair(self.vec, i, j))
