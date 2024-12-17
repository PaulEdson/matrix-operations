import random
import numpy as np

class matrix:
    # takes in rows and columns and creates a random matrix with those dimensions
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.__nums = np.array([], dtype= 'f')
        for i in range(rows*cols):
            self.__nums = np.append(self.__nums, random.randint(0,10))
        self.__matrix = self.__nums.reshape(rows, cols)

    #calling this method returns private matrix data
    def getMatrix(self):
        return self.__matrix

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

    def saveToFile(self):
        f = open('./matrixFile.txt', 'w')
        f.write(str(self.__matrix.tolist()))
        f.close()
    
    def readFromFile(self):
        f = open('matrixFile.txt', 'r')
        self.readArray = np.array((eval(f.read())))
        f.close()
Matrix1 = matrix(3, 3)
Matrix1.saveToFile()
Matrix1.readFromFile()
print(Matrix1.readArray)
print(Matrix1.getMatrix())