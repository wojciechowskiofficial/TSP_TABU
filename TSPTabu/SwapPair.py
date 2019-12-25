"""
this class is complex data type ment to be used for storing alternative solution vector
created from the current solution vector by swapping a pair of vertices.

we assume that first/last vector element is fixed and not swappable!
"""

from TSPCoreComponents.Vertex import Vertex
from copy import deepcopy
from TSPCoreComponents.Computer import Computer

class SwapPair:
    def __init__(self, vec: list(), first: int(), second: int()):
        self.first = first
        self.second = second
        self.vec = deepcopy(vec)
        self.swap()
        self.vec.objFunctValue = Computer.overVec(self.vec)



    def swap(self):
        #(a, b) = (self.vec.get_id(self.first), self.vec.get_id(self.second))
        (a, b) = (self.vec[self.first], self.vec[self.second])
        print(type(self.first))
        #(self.vec[a], self.vec[b]) = (self.vec[b], self.vec[a])
        (self.vec[self.first], self.vec[self.second]) = (b, a)
