"""
this class is complex data type ment to be used for storing a pair of vertices
that are potentially going to be swapped.
"""

from TSPCoreComponents.Vertex import Vertex

class SwapPair:
    self.first = Vertex()
    self.second = Vertex()
    
    def __init__(self, first, second):
        self.first = first
        self.second = second