import matrix
import re

def readMatrixInput(input):
    userInput = input
    userInput.strip()
    userInput = userInput [1:-1]
    rows = re.findall(r'\[(.*?)\]', userInput)
    col = rows[0].split(',')
    matrixRow = []
    matrix = []
    for row in rows:
        for col in row.split(','):
            matrixRow.append(int(col))
        matrix.append(matrixRow)
        matrixRow = []
    return matrix


input = input("enter your first matrix:\n")
formattedInput = readMatrixInput(input)
matrix1 = matrix.matrix.fromArray(formattedInput)
print(matrix1)
print(matrix1.getMatrix())
