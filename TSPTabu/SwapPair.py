"""
this class is complex data type ment to be used for storing alternative solution vector
created from the current solution vector by swapping a pair of vertices.
"""

from TSPCoreComponents.Vertex import Vertex

class SwapPair:
    def __init__(self, vec: list[Vertex], first: int(), second: int()):
        self.first = first
        self.second = second
        self.vec = vec
        self.swap()


    def swap(self):
        (a, b) = (self.vec.index(self.first), self.vec.index(self.second))
        (self.vec[a], self.vec[b]) = (self.vec[b], self.vec[a])
