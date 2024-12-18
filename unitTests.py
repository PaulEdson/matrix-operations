import unittest
import matrix

class TestMatrixMethods(unittest.TestCase):

    #checks that base constructor can run given clean parameters
    def testConstructor(self):
        myMatrix = matrix.matrix([1,2,3,4,5,6,7,8,9], 3, 3)
        self.assertEqual([[1,2,3],[4,5,6],[7,8,9]], myMatrix.getMatrix().tolist())
    
    #checks whether random is creating matrices of the correct shape
    def testRandom(self):
        myMatrix = matrix.matrix.random(3,3)
        self.assertEqual(myMatrix.getMatrix().shape, (3, 3))

    #writes a matrix to a specified file, then reads the file. Checks these two matrices contain the same values
    def testWriteRead(self):
        myWriteMatrix = matrix.matrix.random(3,3)
        myWriteMatrix.saveToFile('matrixTestFile.txt')
        myReadMatrix = matrix.matrix.fromFile('matrixTestFile.txt')
        self.assertEqual(myWriteMatrix.getMatrix().all(), myReadMatrix.getMatrix().all())

    #test for identity matrix class method
    def testidentityMatrix(self):
        myMatrix = matrix.matrix.identity(3)
        self.assertEqual([[1,0,0],[0,1,0],[0,0,1]], myMatrix.getMatrix().tolist())

    #test for zero matrix class method
    def testZeroMatrix(self):
        myMatrix = matrix.matrix.zero(4, 3)
        self.assertEqual([[0,0,0],[0,0,0],[0,0,0],[0,0,0]], myMatrix.getMatrix().tolist())
    
    #makes sure that matrix.addmatrix does not raise any errors when running
    def testAddition(self):
        myMatrix1 = matrix.matrix.random(3, 4)
        myMatrix2 = matrix.matrix.random(3, 4)
        sumMatrix = myMatrix1.addMatrix(myMatrix2)
        self.assertEqual(sumMatrix.getMatrix().tolist()[0][0], myMatrix1.getMatrix()[0][0] + myMatrix2.getMatrix()[0][0] )
    
    #matrices with different dimensions cannot be added or subtracted without raising a value error. 
    def testAdditionIncorrectParam(self):
        myMatrix1 = matrix.matrix.random(4, 4)
        myMatrix2 = matrix.matrix.random(3, 4)
        sumMatrix = myMatrix1.addMatrix(myMatrix2)
        self.assertRaises(ValueError)
    
    #checks that matrix.subtractMatrix works when passed clean parameters
    def testSubtraction(self):
        myMatrix1 = matrix.matrix.random(5, 2)
        myMatrix2 = matrix.matrix.random(5, 2)
        diffMatrix = myMatrix1.subtractMatrix(myMatrix2)
        self.assertEqual(diffMatrix.getMatrix().tolist()[0][0], myMatrix1.getMatrix()[0][0] - myMatrix2.getMatrix()[0][0] )
    
    #a value error should be raised when matrices of different sizes are passed
    def testSubtractionIncorrectParam(self):
        myMatrix1 = matrix.matrix.random(4, 4)
        myMatrix2 = matrix.matrix.random(3, 4)
        diffMatrix = myMatrix1.subtractMatrix(myMatrix2)
        self.assertRaises(ValueError)
    
    def testMultiplication(self):
        myMatrix1 = matrix.matrix.random(3, 4)
        myMatrix2 = matrix.matrix.random(4, 3)
        multMatrix = myMatrix1.multiplyMatrix(myMatrix2)
    
    def testMultiplitcationIncorrectParam(self):
        myMatrix1 = matrix.matrix.random(3, 4)
        myMatrix2 = matrix.matrix.random(3, 3)
        multMatrix = myMatrix1.multiplyMatrix(myMatrix2)
        self.assertRaises(ValueError)
    
    
if __name__ == "__main__":
    unittest.main()