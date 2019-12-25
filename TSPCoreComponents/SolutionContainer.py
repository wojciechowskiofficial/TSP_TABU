class SolutionContainer:
    def __init__(self):
        self.verticesVector = list()
        """
        objFunctValue (objective function value)
        summary distance created online by travelling salesman
        is to be minimalized
        initiated with float(0) due to the aggregational nature
        """
        self.objFunctValue = 0

    def __str__(self):
        string = str()
        for el in self.verticesVector:
            string += str(el)
            string += '\n'
        string += '\n'
        string += 'objective function value: '
        string += str(self.objFunctValue)
        return string

    def __repr__(self):
        return self.__str__()

    def __len__(self):
        return len(self.verticesVector)

    def __getitem__(self, item):
        return self.verticesVector[item]

    def __setitem__(self, key, value):
        self.verticesVector[key] = value

    def get_id(self, x):
        for i in range(len(self.verticesVector) - 1):
            if self.verticesVector[i].id == x:
                return i
        return -1
