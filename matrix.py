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

    #can pass generated arrays into this classmethod to create new matrix objects
    @classmethod
    def fromArray(cls, arr):
        arr = np.array(arr)
        try:
            rows = arr.shape[0]
            cols = arr.shape[1]
        except Exception as e:
            print("2D array should be passed into this method")
            return
        list = arr.reshape(-1)
        return cls(list, rows, cols)

    #initializes matrix with random numbers between 1-10
    @classmethod
    def random(cls, rows, cols):
        numList = []
        for i in range(rows*cols):
            numList.append(random.randint(1, 10))
        return cls(numList, rows, cols)
    
    #read matrix from text file
    #stored matrices are in python list format, so eval can be used
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
        try:
            return matrix.fromArray(np.add(self.__matrix, passedMatrix.getMatrix()).tolist())
        except ValueError:
            print("These matrices cannot be added")
    def subtractMatrix(self, passedMatrix):
        try:
            return matrix.fromArray(np.subtract(self.__matrix, passedMatrix.getMatrix()).tolist())
        except ValueError:
            print("matrices must be of the same shape to be added or subtracted")
            return

    #matrices can only be multiplied if the length of rowsA matches columnsB
    #returns a matrix object
    def multiplyMatrix(self, passedMatrix):
        try:
            return matrix.fromArray(np.dot(self.__matrix, passedMatrix.getMatrix()).tolist())
        except ValueError:
            print("the length of Matrix A's columns must match the length of Matrix B's rows for matrix multiplication")

    #any matrix can be transposed
    #returns a matrix object
    def transpose(self):
        return matrix.fromArray(np.transpose(self.__matrix).tolist())

    #only calculable for square matrices
    #returns a number (float or int)
    def getDeterminant(self):
        try:
            return np.linalg.det(self.__matrix)
        except ValueError:
            if (self.__matrix.shape[0] != self.__matrix.shape[1]):
                print("Must pass in square matrix for determinant calculation")
            else:
                print(Exception)
            return
        except Exception as e:
            print(e)
            return
        
    #only calculable for square matrices
    #returns matrix object
    def getInverse(self):
        try:
            return matrix.fromArray(np.linalg.inv(self.__matrix).tolist())
        except ValueError:
            if(self.__matrix.shape[0] != self.__matrix.shape[1]):
                print("Must pass in square matrix for inverse calculation")
            elif(self.getDeterminant() == 0):
                print("determinant is zero: invalid inverse target")
            return
        except Exception as e:
            print(e)
            return
    
    #does not work for non-square matrices
    #returns the decomposition matrices that when multiplied should equal the original matrix
    def eigenDecomp(self):
        try:
            eigValues, eigVectors = np.linalg.eig(self.__matrix)
            D = matrix.fromArray(np.diag(eigValues).tolist())
            R = matrix.fromArray(eigVectors)
            Rinverse = R.getInverse()
            return R, D, Rinverse
        except ValueError:
            if(self.__matrix.shape[0] != self.__matrix.shape[1]):
                print("Must pass in square matrix for eigen decomposition calculation")
            else:
                print(Exception)
            return
        except Exception as e:
            print(e)
            return

    #saves matrix to file. Currently overwrites anything else on file.
    def saveToFile(self, file):
        f = open(file, 'w')
        f.write(str(self.__matrix.tolist()))
        f.close()

    #displays matrix as a heatmap using seaborn
    def toHeatMap(self):
        sns.heatmap(self.__matrix, cmap='viridis', annot=True)
        plt.show()

matrix1 = matrix.random(3,4,5)