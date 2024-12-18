import random
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class matrix:
    #most basic constructor that all initializing class methods call
    def __init__(self, passedList, rows, cols):
        self.__rows = rows
        self.__cols = cols
        self.__nums = passedList
        self.__nums = np.array(self.__nums, dtype = 'f')
        self.__matrix = self.__nums.reshape(self.__rows, self.__cols)

    #initializes matrix with random numbers between 1-10
    @classmethod
    def random(cls, rows, cols):
        numList = []
        for i in range(rows*cols):
            numList.append(random.randint(1, 10))
        return cls(numList, rows, cols)
    
    #read matrix from text file
    @classmethod
    def fromFile(cls, file):
        f = open(file, 'r')
        try:
            list = eval(f.read())
        except:
            print("passed file is not in the correct format. Pass in an array of the format [[],[]]")
            f.close()
            return
        f.close()
        list = np.array(list)
        try:
            rows = list.shape[0]
            cols = list.shape[1]
        except:
            print('Pass in a matrix of the format [[1,2],[3,4]] or [[1, 2, 3]] if 1 dimensional')
            return
        list = list.reshape(-1)
        return cls(list, rows, cols)
    
    #initializes matrix as identity matrix. needs a given dimension
    @classmethod
    def identity(cls, rows):
        numList = []
        for i in range(rows):
            for j in range(rows):
                if(j==i):
                    numList.append(1)
                else:
                    numList.append(0)
        return cls(numList, rows, rows)
    
    #initialize matrix as zero matrix when called, takes rows and columns as arguments
    @classmethod
    def zero(cls, rows, cols):
        numList = []
        for i in range(rows*cols):
            numList.append(0)
        return cls(numList, rows, cols)

    #getter and setter methods
    def getMatrix(self):
        return self.__matrix

    def getDimmensions(self):
        return [self.__rows, self.__cols]

    def setMatrix(self, passedMatrix):
        self.__matrix = passedMatrix

    #passedMatrix must be a matrix class object
    #add and subtract matrices must be of the same dimensions
    def addMatrix(self, passedMatrix):
        return np.add(self.__matrix, passedMatrix.getMatrix())

    def subtractMatrix(self, passedMatrix):
        return np.subtract(self.__matrix, passedMatrix.getMatrix())

    #matrices can only be multiplied if the length of rowsA matches columnsB
    def multiplyMatrix(self, passedMatrix):
        return np.dot(self.__matrix, passedMatrix.getMatrix())

    #any matrix can be transposed
    def transpose(self):
        return np.transpose(self.__matrix)

    #only calculable for square matrices
    def getDeterminant(self):
        return np.linalg.det(self.__matrix)

    #any matrix can have an inverse
    def getInverse(self):
        return np.linalg.inv(self.__matrix)

    #does not work for non-square matrices
    def eigenDecomp(self):
        return np.linalg.eig(self.__matrix)

    #saves matrix to file. Currently overwrites anything else on file.
    def saveToFile(self):
        f = open('./matrixFile.txt', 'w')
        f.write(str(self.__matrix.tolist()))
        f.close()

    #displays matrix as a heatmap using seaborn
    def toHeatMap(self):
        sns.heatmap(self.__matrix, cmap='viridis', annot=True)
        plt.show()



matrix1 = matrix.random(3,3)
print(matrix1.getMatrix())
matrix1.setMatrix(matrix1.getInverse())
matrix1.toHeatMap()