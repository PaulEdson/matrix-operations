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
    
    #for now just makes sure that multiplying throws no errors
    def testMultiplication(self):
        myMatrix1 = matrix.matrix.random(3, 4)
        myMatrix2 = matrix.matrix.random(4, 3)
        multMatrix = myMatrix1.multiplyMatrix(myMatrix2)
    
    #purposefully multiplies incompatable matrices to make sure a ValueError is raised correctly
    def testMultiplitcationIncorrectParam(self):
        myMatrix1 = matrix.matrix.random(3, 4)
        myMatrix2 = matrix.matrix.random(3, 3)
        multMatrix = myMatrix1.multiplyMatrix(myMatrix2)
        self.assertRaises(ValueError)
    
    #Checks that matrix.transpose correctly transposes matrices
    def testTranspose(self):
        myMatrix1 = matrix.matrix.random(2, 3)
        myMatrix2 = myMatrix1.transpose()
        for row in range(len(myMatrix1.getMatrix())):
            for col in range(len(myMatrix1.getMatrix()[row])):
                self.assertEqual(myMatrix1.getMatrix()[row][col], myMatrix2.getMatrix()[col][row])
    
    #Makes sure matrix.getDeterminant does not error out or return a None value when good parameters are passed
    def testDeterminate(self):
        myMatrix1 = matrix.matrix.random(4, 4)
        determinate = myMatrix1.getDeterminant()
        self.assertFalse(type(determinate) is None)
    
    #Ensures a value error is raised when a non-square matrix is passed to getDeterminate
    def testDeterminateIncorrectParam(self):
        myMatrix1 = matrix.matrix.random(3, 4)
        determinate = myMatrix1.getDeterminant()
        self.assertRaises(ValueError)
    
    #ensures that getInverse * its orginal matrix returns the identity matrix and produces no errors
    def testInverse(self):
        myMatrix1 = matrix.matrix([1, 2, 3, 4, 5, 6, 6, 8, 9], 3, 3)
        myInverseMatrix = myMatrix1.getInverse()
        productMatrix = myMatrix1.multiplyMatrix(myInverseMatrix)
        identityMatrix = matrix.matrix.identity(3)
        self.assertAlmostEqual(productMatrix.getMatrix().all(), identityMatrix.getMatrix().all())
    
    #Should raise a ValueError that prints a warning of zero determinate
    def testInverseZeroDet(self):
        myMatrix1 = matrix.matrix([1,2,3,4,5,6,7,8,9],3,3)
        myMatrix1.getInverse()
        self.assertRaises(ValueError)
    
    #should raise a ValueError that prints a warning or non-square matrix
    def testInverseIncorrectShape(self):
        myMatrix1 = matrix.matrix.random(1,5)
        myMatrix1.getInverse()
        self.assertRaises(ValueError)
    
    #Testing to make sure no errors are thrown when given good data
    #tests that decomposition is equal to original matrix
    def testEigenDecomp(self):
        #added loop to remake the matrix if it creates onw with no determinate and an invalid inverse
        R, D, Rinverse = [None, None, None]
        while Rinverse == None:
            myMatrix1 = matrix.matrix.random(3, 3)
            R, D, Rinverse = myMatrix1.eigenDecomp()
        self.assertAlmostEqual(R.multiplyMatrix(D.multiplyMatrix(Rinverse)).getMatrix().all(), myMatrix1.getMatrix().all())
    
    #ValueError should be raised when non-zero matrix is passed to matrix.eigenDecomp
    def testEigenDecompIncorrectShape(self):
        myMatrix1 = matrix.matrix.random(4,3)
        myMatrix1.eigenDecomp()
        self.assertRaises(ValueError)
    

if __name__ == "__main__":
    unittest.main()