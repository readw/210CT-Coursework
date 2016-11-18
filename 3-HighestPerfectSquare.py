# Week 2 - 3) Write pseudocode for a function which returns the highest perfect
#             square which is less or equal to its parameter (a positive
#             integer). Implement this in a programming language of your choice.

'''
PSEUDOCODE
----------
HIGHEST_PERFECT_SQUARE(N):
    perfectSquare <- 1
    
    FOR i IN range(1, N)
        IF N - i^2 >= 0
            perfectSquare = i
        ELIF N - i^2 < 0
            BREAK FOR
        END IF
    END FOR

    RETURN perfectSquare
'''

def HighestPerfectSquare(N):
    '''Calculates the Highest Perfect Square that can be retrieved from a
passed integer.'''
    # Default HighestPerfectSquare to 0.
    perfectSquare = 1

    for i in range(1, N):
        # Check if value is able to be subtracted by square of i.
        if N - i**2 >= 0:
            #Set perfect square to i.
            perfectSquare = i
            
        # If square less than 0 exit search.
        elif N - i**2 < 0:
            break

    return perfectSquare

if __name__ == "__main__":
    while True:
        try:
            # Enter a integer value.
            number = int(input("Enter a number: "))

            # Determine the highest perfect square.
            print("Highest Perfect Square: "+str(HighestPerfectSquare(number)))
        except:
            break
