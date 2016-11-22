# Week 3 - 7) Write the recursive function (pseudocode and code) to check if
#             a number (n) is prime.

'''
PSEUDOCODE
----------
RECURSIVE_PRIME(N, M)
    IF M = 1
        RETURN TRUE
    IF N%M = 0
        RETURN FALSE
    ELSE
        RETURN PRIME(N, M-1)

'''

def RecursivePrime(Number, Minus):
    '''Determines if a passed number is in reverse order.'''         # Example: n=3
    # If N is 1 or 2 then it is a Prime Number.
    if Minus == 1 or Minus == 0:                                     # O(1) --> O(1)
        return True                                                  # O(1) --> O(1)
    # Checks if there isn't a remainder between N and M.
    # Therefore it isn't a prime.
    if Number % Minus == 0:                                          # O(1) --> O(1)
        return False                                                 # O(1) --> O(1)
    else:                                                            # O(1) --> O(1)
        # If neither match re-call function and take one from M.
        return RecursivePrime(Number, Minus-1)                       # O(n) --> O(3)

if __name__ == "__main__":
    while True:
        try:
            # User enters a number.
            number = int(input("Please input a number: "))
            # Return result of Recursive Prime.
            print(RecursivePrime(number, number-1))
        except:
            break
