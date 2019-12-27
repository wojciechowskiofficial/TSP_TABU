class TabuMatrix:
    def __init__(self, size):
        self.size = size
        self.matrix = list()
        for i in range(self.size):
            self.matrix.append(list())
            for j in range(self.size):
                self.matrix[i].append(0)

    def __str__(self):
        return '\n'.join([str(row) for row in self.matrix])

    def __repr__(self):
        return self.__str__()

    def set(self, i, j, value):
        (i, j) = self.checkSecurity(i, j)
        self.matrix[i][j] = value

    def get(self, i, j):
        (i, j) = self.checkSecurity(i, j)
        return self.matrix[i][j]

    #method which ensures that element indicated by i and j is in upper triangular matrix
    #excluding main diagonal of the matrix
    def checkSecurity(self, _i, _j):
        if _i > _j:
            (i, j) = (_j, _i)
        else:
            (i, j) = (_i, _j)
        if i == j:
            raise IndexError('tabu matrix ids cannot indicate main diagonal matrix position')
        return (i, j)
