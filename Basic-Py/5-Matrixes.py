# Week 2 - 5) Write the pseudocode corresponding to functions for addition,
#             subtraction and multiplication of two matrices, and then compute
#             A = B*C-2*(B+C) where B and C are two quadratic matrices of order
#             n. What is the run-time?

'''
PSEUDOCODE
----------
ADD_MATRIX(B, C)
    resultMatrix <- []
    FOR i IN range(length of B)
        APPEND [] TO resultMatrix
        FOR j IN range(length of C[0])
            APPEND B[i][j] + C[i][j] TO resultMatrix[i]

SUB_MATRIX(B, C)
    resultMatrix <- []
    FOR i IN range(length of B)
        APPEND [] TO resultMatrix
        FOR j IN range(length of C[0])
            APPEND B[i][j] - C[i][j] TO resultMatrix[i]

MULTI_MATRIX(B, C)
    resultMatrix <- []
    FOR i IN range(length of B)
    APPEND [] TO resultMatrix
        FOR j IN range(length of C[0])
            APPEND 0 TO resultMatrix[i]
            FOR k IN range(length of C)
                resultMatrix <- resultMatrix + (B[i][k] * C[k][j])
'''

def addMatrix(matrixOne, matrixTwo):
    '''Takes two Matrix and adds them together to get a result.'''                      # Example: n=3
    resultMatrix = []                                                                   # O(1)   --> O(1)
    # Check length of the first Matrix
    for x in range(len(matrixOne)):                                                     # O(n)   --> O(3)
        resultMatrix.append([])                                                         # O(n)   --> O(3)
        # Check height of the second Matrix
        for y in range(len(matrixTwo[0])):                                              # O(n^2) --> O(9)
            # Add the values at the same positions together to get result.
            resultMatrix[x].append(int(matrixOne[x][y]) + int(matrixTwo[x][y]))         # O(n^2) --> O(9)
            
    # Return Added Matrix Result
    return resultMatrix                                                                 # O(1)   --> O(1)

def subMatrix(matrixOne, matrixTwo):
    '''Takes two Matrix and subtracts them from each other.'''                          # Example: n=2
    resultMatrix = []                                                                   # O(1)   --> O(1)
    # Check length of the first Matrix
    for x in range(len(matrixOne)):                                                     # O(n)   --> O(2)
        resultMatrix.append([])                                                         # O(n)   --> O(2)
        # Check height of the second Matrix
        for y in range(len(matrixOne[0])):                                              # O(n^2) --> O(4)
            # Subtract the values at the same positions from each other to get result.
            resultMatrix[x].append(int(matrixOne[x][y]) - int(matrixTwo[x][y]))         # O(n^2) --> O(4)

    # Return Subtracted Matrix.
    return resultMatrix                                                                 # O(1)   --> O(1)

def multiMatrix(matrixOne, matrixTwo):
    '''Takes two Matrix values and multiplys them together.'''                          # Example: n=2
    resultMatrix = []                                                                   # O(1)   --> O(1)
    # Check length of the first Matrix
    for x in range(len(matrixOne)):                                                     # O(n)   --> O(2)
        resultMatrix.append([])                                                         # O(n)   --> O(2)
        # Check height of the second Matrix
        for y in range(len(matrixTwo[0])):                                              # O(n^2) --> O(4)
            resultMatrix[x].append(0)                                                   # O(n^2) --> O(4)
            # Check the length of MatrixTwo.
            for k in range(len(matrixTwo)):                                             # O(n^3) --> O(8)
                # Multiply all the values in row of matrixOne and column of matrixTwo
                # together.
                resultMatrix[x][y] += int(matrixOne[x][k])*int(matrixTwo[k][y])         # O(n^3) --> O(8)

    # Returns Multiplyed Matrix.
    return resultMatrix                                                                 # O(1)   --> O(1)

def equationMatrix(B, C):
    '''Calculates the equation A=B*C-2*(B+C)'''
    # Part 1 = B+C
    result1 = addMatrix(B, C)

    # Part 2 = B*C
    result2 = multiMatrix(B, C)

    # Part 3 = 2*Part 1
    result3 = addMatrix(result1, result1)

    # Answer = Part 2 - Part 3
    answer = subMatrix(result2, result3)

    return answer

if __name__ == "__main__":
    while True:
        try:
            # Determine the number of rows.
            print("---MATRIX ROWS---")
            rows = 0
            while rows <= 0:
                rows = int(input("Number of rows: "))
                if rows == 0:
                    print("NEED 1 OR MORE ROWS.")

            # Determine the values within the first Matrix
            print("\n---MATRIX 1---")
            matrixOne = []
            for row in range(rows):
                data = input("Enter numerical values (split by ','): ").split(',')
                matrixOne.append(data)

            # Determine the values within the second Matrix
            print("\n---MATRIX 2---")
            matrixTwo = []
            for row in range(rows):
                data = input("Enter numerical values (split by ','): ").split(',')
                matrixTwo.append(data)

            # Perform the following calculation.
            print("B*C-2(B+C)="+str(equationMatrix(matrixOne, matrixTwo)))
        except:
            break
