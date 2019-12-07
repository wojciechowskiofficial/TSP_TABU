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