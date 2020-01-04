from FileHandler.InstanceGenerator import InstanceGenerator
from FileHandler.FileReader import FileReader
from TSPTabu.Tabu import Tabu

class Benchmark:
    def __init__(self, start, nrOfMeasurements, incrementSize):
        self.start = start
        self.nrOfMeasurements = nrOfMeasurements
        self.incrementSize = incrementSize
        self.greedy = list()
        self.tabu = list()
        self.sizeList = [x for x in range(self.start, self.start + self.nrOfMeasurements * self.incrementSize, self.incrementSize)]

    def compGreedyTabu(self):
        size = self.start
        for i in range(self.nrOfMeasurements):
            generator = InstanceGenerator(size)
            generator.generate()
            generator.assembleFileName()
            scan = FileReader(generator.fileName)
            scan.importInstance()
            instance = scan.instance
            solve = Tabu(instance, auto = True)
            solve.solveTabu()
            self.greedy.append(solve.greedySolution.objFunctValue)
            self.tabu.append(solve.globallyOptimal.objFunctValue)
            size += self.incrementSize
        self.iterGreedy = iter(self.greedy)
        self.iterTabu = iter(self.tabu)

    def saveToFile(self):
        name = 'benchmark_' + str(self.start) + '_' + str(self.nrOfMeasurements) + '_' + str(self.incrementSize) + '.txt'
        print(self.sizeList)
        print(len(self.sizeList), len(self.greedy))
        with open(name, 'w') as f:
            for size in self.sizeList:
                f.write(str(size))
                f.write(',')
                f.write(str(next(self.iterGreedy)))
                f.write(',')
                f.write(str(next(self.iterTabu)))
                f.write('\n')
