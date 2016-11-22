# Week 2 - 4) Look back at last week's tasks. Describe the run-time bounds of
#             these algorithms using BigO notation.

'''
WEEK 1 - 1)
-----------
def Randomise(array):
    randomArray = []                             O(1)        --> O(1)
    
    while len(array) != 0:                       O(n)        --> O(2)
        randomInt = randint(0, len(array)-1)     O(n*log(n)) --> O(2*log(2))
        randomArray.append(array[randomInt])     O(n*log(n)) --> O(2*log(2))
        array.remove(array[randomInt])           O(n*log(n)) --> O(2*log(2))
        
    return randomArray                           O(1)        --> O(1)


WEEK 1 - 2)
-----------
def Factorial(N):
    noZeros = 0                                  O(1)        --> O(1)

    for i in range(1, N):                        O(n)        --> O(2)
        noZeros += int(N//(5**i))                O(n)        --> O(2)

    return noZeros                               O(1)        --> O(1)


WEEK 2 - 3)
-----------
def HighestPerfectSquare(N):
    perfectSquare = 1                            O(1)        --> O(1)
    
    for i in range(1, N):                        O(n)        --> O(2)
        if N - i**2 >= 0:                        O(n)        --> O(2)
            perfectSquare = i                    O(n)        --> O(2)
        elif N - i**2 < 0:                       O(n)        --> O(2)
            break                                O(n)        --> O(2)
        
    return perfectSquare                         O(1)        --> O(1)
'''
