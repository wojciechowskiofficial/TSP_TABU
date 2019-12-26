"""
this class is complex data type ment to be used for storing alternative solution vector
created from the current solution vector by swapping a pair of vertices.

we assume that first/last vector element is fixed and not swappable!
"""

from copy import deepcopy
from TSPCoreComponents.Computer import Computer

class SwapPair:
    def __init__(self, vec: list(), first: int(), second: int()):
        #constraints for first and second
        # 0 < first, second < len(vec) - 1
        if first <= 0 or first >= len(vec) - 1 or second <= 0 or second >= len(vec) - 1:
            raise IndexError('SwapPair swap elements out of bounds, violating problem assumptions')
        self.first = first
        self.second = second
        self.vec = deepcopy(vec)
        self.swap()
        self.vec.objFunctValue = Computer.overVec(self.vec)
        self.objFunctValue = self.vec.objFunctValue

    def swap(self):
        (a, b) = (self.vec[self.first], self.vec[self.second])
        (self.vec[self.first], self.vec[self.second]) = (b, a)