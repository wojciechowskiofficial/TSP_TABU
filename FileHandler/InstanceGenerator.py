import random
import os

class InstanceGenerator:
    def __init__(self, size, constrains = None):
        self.size = size
        if constrains is None:
            self.constrains = size * 1000
        else:
            self.constrains = constrains
        self.fileName = None
        self.pathName = None

    def assembleFileName(self):
        string = 'gen_size_'
        string += str(self.size)
        string += '_constrains_'
        string += str(self.constrains)
        string += '.txt'
        self.fileName = string

    def createPath(self):
        if not os.path.exists('IOFiles'):
            os.makedirs('IOFiles')
        #possible error when self.fileName was not created beforehand
        try:
            self.pathName = 'IOFiles/' + self.fileName
        except TypeError:
            self.assembleFileName()
            self.pathName = 'IOFiles/' + self.fileName

    def generate(self):
        if self.fileName is None:
            self.assembleFileName()
        if self.pathName is None:
            self.createPath()
        with open(self.pathName, 'w') as f:
            f.write(str(self.size))
            f.write('\n')
            for i in range(self.size):
                f.write(str(i + 1))
                f.write(' ')
                f.write(str(random.randint(0, self.constrains)))
                f.write(' ')
                f.write(str(random.randint(0, self.constrains)))
                f.write('\n')

