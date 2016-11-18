# Week 2 - 4) Look back at last week's tasks. Describe the run-time bounds of
#             these algorithms using BigO notation.

'''
WEEK 1 - 1)
-----------
def Randomise(array):
    randomArray = []                             O(n) --> O(2)
    
    while len(array) != 0:                       O(n) --> O(2)
        randomInt = randint(0, len(array)-1)     O(n) --> O(2)
        randomArray.append(array[randomInt])     O(n) --> O(2)
        array.remove(array[randomInt])           O(n) --> O(2)
        
    return randomArray                           O(n) --> O(2)


WEEK 1 - 2)
-----------
def Factorial(N):
    noZeros = 0

    for i in range(1, N):
        noZeros += int(N//(5**i))

    return noZeros


WEEK 2 - 3)
-----------
def HighestPerfectSquare(N):
    perfectSquare = 1
    for i in range(1, N):
        if N - i**2 >= 0:
            perfectSquare = i
        elif N - i**2 < 0:
            break
        
    return perfectSquare
'''
