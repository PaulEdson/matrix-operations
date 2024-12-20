import matrix
import re

#used to read input matrices when given as 2D lists
def readMatrixInput(userInput):
    userInput = userInput
    userInput.strip()
    userInput = userInput [1:-1]
    rows = re.findall(r'\[(.*?)\]', userInput)
    col = rows[0].split(',')
    matrixRow = []
    matrixList = []
    for row in rows:
        for col in row.split(','):
            matrixRow.append(float(col))
        matrixList.append(matrixRow)
        matrixRow = []
    return matrixList

#parses whether given matrix is a file location, generating command, or 2D list
def matrixInputSequence(userInput):
    try:
        paramList = []
        command = userInput.split(':')[0]
        args = userInput.split(':')[1]
        if command == 'random':
            for arg in args.split():
                paramList.append(int(arg))
            rMatrix = matrix.matrix.random(paramList[0], paramList[1])
        elif command == 'identity':
            paramList.append(int(args))
            rMatrix = matrix.matrix.identity(paramList[0])

    except:
        try:
            rMatrix = matrix.matrix.fromFile(userInput)
        except:
            try:
                formattedInput = readMatrixInput(userInput)
                rMatrix = matrix.matrix.fromArray(formattedInput)
            except:
                print("list not recognized")
                return
    return rMatrix

#main method runs until exit is typed into the command line
def main():
    print("Type \"help\" to get a list of commands\n")
    userInput = None
    matrix1 = None

    #case switch contains all commands available to the calculator
    while userInput != 'exit':
        match userInput:
            case '+':
                try:
                    userInput = input("enter a matrix to add:\n")
                    matrix2 = matrixInputSequence(userInput)
                    matrix1 = matrix1.addMatrix(matrix2)
                    print("sum:\n", matrix1.getMatrix())
                except:
                    if matrix1 == None:
                        print('+ does not work as no matrix has been given')
            case '-':
                try:
                    userInput = input("enter a matrix to subtract:\n")
                    matrix2 = matrixInputSequence(userInput)
                    matrix1 = matrix1.subtractMatrix(matrix2)
                    print("difference:\n", matrix1.getMatrix())
                except:
                    if matrix1 == None:
                        print('- does not work as no matrix has been given')
            case '*':
                try:
                    userInput = input("enter a matrix to multiply by:\n")
                    matrix2 = matrixInputSequence(userInput)
                    matrix1 = matrix1.multiplyMatrix(matrix2)
                    print("product-", end="")
                except:
                    if matrix1 == None:
                        print('* does not work as no matrix has been given')
            case 'display':
                try:
                    matrix1.toHeatMap()
                except:
                    if matrix1 == None:
                        print('transpose does not work as no matrix has been given')
            case 'transpose':
                try:
                    matrix1 = matrix1.transpose()
                    print('transposed-', end = "")
                except:
                    if matrix1 == None:
                        print('transpose does not work as no matrix has been given')

            case 'inverse':
                try:
                    matrix1 = matrix1.getInverse()
                    print('inversed-', end = "")
                except:
                    if matrix1 == None:
                        print('inverse does not work as no matrix has been given')
            
            case 'determinant':
                try:
                    print(matrix1.getDeterminant())
                except:
                    if matrix1 == None:
                        print('determinant does not work as no matrix has been given')
                
            case 'save':
                try:
                    matrix1.saveToFile('savedMatrix.txt')
                except:
                    if matrix1 == None:
                        print('save does not work as no matrix has been given')
            
            case 'eigDecomp':
                try:
                    R, D, Rinverse = matrix1.eigenDecomp()
                    print('Eigen decomposition below. The products of these matrices should equal the input matrix:')
                    print(R.getMatrix(),'\n * \n', D.getMatrix(),'\n * \n', Rinverse.getMatrix())
                except:
                    if matrix1 == None:
                        print('eigDecomp does not work as no matrix has been given')
            case 'clear':
                print("cleared")
                matrix1 = None
            
            case 'help':
                print("To enter a matrix you want to perform calculations, type in either a 2D array of the form:\
                      \n[[1,2,3],[4,5,6],[7,8,9]]\nOr you may enter the file location and name of a file containing",
                       "the same text")
                print("Matrix generation commands:\n-random:<int rows> <int columns> \n-identity:<int size>\
                        \nTo clear the current matrix and enter a new one type: \n-clear \
                        \nTo save a matrix to a file called matrixFile.txt: \n-save\
                        \nOther Commands: \
                        \n- + - Add a given matrix \
                        \n- - - subtract a given matrix \
                        \n- * - multiply by a given matrix \
                        \n- transpose - transpose the matrix already given \
                        \n- inverse - inverse the matrix already given \
                        \n- determinant - display the determinant of matrix already given \
                        \n- eigDecomp - display the eigen decomposition matrices of matrix already given \
                        \n- display - show matrix already given in a seaborn heatmap")
            case _:
                print('command not recognized')
        #if a matrix is stored, ask what operations the user would like to perform on it
        if matrix1 != None: 
            print("formatted matrix:\n", matrix1.getMatrix())
            userInput = input("Enter the desired operation:\n")
        #if no matrix is stored, one needs to be given
        else:
            userInput = input("enter your first matrix in the format: [[1,2,3],[4,5,6]...]\n")
            matrix1 = matrixInputSequence(userInput)

#main method call
if __name__ == "__main__":
    main()