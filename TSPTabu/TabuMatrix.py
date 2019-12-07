class TabuMatrix:
    def __init__(self, size):
        self.size = size
        self.matrix = list()
        for i in range(self.size):
            self.matrix.append(list())
            for j in range(self.size):
                self.matrix[i].append(0)

    def set(self, i, j, value):
        if self.matrix is not None:
            self.matrix[i][j] = value
        else:
            raise IndexError

    def get(self, i, j):
        if self.matrix is not None:
            return self.matrix[i][j]
        else:
            raise IndexError
