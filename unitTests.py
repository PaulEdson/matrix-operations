import unittest
import matrix

class TestMatrixMethods(unittest.TestCase):

    def testConstructor(self):
        myMatrix = matrix.matrix([1,2,3,4,5,6,7,8,9], 3, 3)
        self.assertEqual([[1,2,3],[4,5,6],[7,8,9]], myMatrix.getMatrix().tolist())
    
    #checks whether random is creating matrices of the correct shape
    def testRandom(self):
        myMatrix = matrix.matrix.random(3,3)
        self.assertEqual(myMatrix.getMatrix().shape, (3, 3))

    def testWriteRead(self):
        myWriteMatrix = matrix.matrix.random(3,3)
        myWriteMatrix.saveToFile('matrixTestFile.txt')
        myReadMatrix = matrix.matrix.fromFile('matrixTestFile.txt')
        print(myWriteMatrix.getMatrix())
        print(myReadMatrix.getMatrix())
        self.assertEqual(myWriteMatrix.getMatrix().all(), myReadMatrix.getMatrix().all())
if __name__ == "__main__":
    unittest.main()