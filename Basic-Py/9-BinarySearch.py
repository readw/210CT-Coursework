# Week 4 - 9) Adapt the binary search algorithm so that instead of outputting
#             whether a specific value was found, it outputs whether a value
#             within a specific interal was found.

'''
PSEUDOCODE
----------
BINARY_SEARCH(L, low, high)
    min <- 0
    max <- (length of L) - 1

    WHILE max-min != 1
        mid <- ((max+min) // 2)-1
        If low < L[mid] < high
            RETURN TRUE
        ELSE
            IF L[mid] < high
                max -= 1
            IF L[mid] > low
                min += 1
                
    RETURN FALSE
'''

def BinarySearch(L, low, high):
    '''Perform a binary search on a collection of data to check if the search
range is within a particular list.'''                                                    # Example: n=3
    # Set minimum pointer as 1.
    minimum = 1                                                                          # O(1) --> O(1)
    # Set maximum pointer as the length of the list.
    maximum = len(L)                                                                     # O(1) --> O(1)

    while minimum + (maximum - minimum) > 0:                                             # O(n) --> O(3)

        # Set the middle value in the remaining list.
        middle = minimum + (maximum-minimum)//2                                          # O(n) --> O(3)
        # If between the range, then search was a success.
        if low < L[middle] < high:                                                       # O(n) --> O(3)
            return True                                                                  # O(n) --> O(3)

        # If the value is higher than the highest point of the range, set the
        # minimum to the top half of the list.
        if L[middle] > high:                                                             # O(n) --> O(3)
            minimum = middle+1                                                           # O(n) --> O(3)

        # If the value is lower then the lowest range, set the maximum point
        # to the lower half of the list.
        if L[middle] < low:                                                              # O(n) --> O(3)
            maximum = middle-1                                                           # O(n) --> O(3)

    # If no value is found returns false.
    return False                                                                         # O(1) --> O(1)

if __name__ == "__main__":
    while True:
        try:
            # Creates a sorted integer array of a list of numbers.
            array = sorted(input("Numbers List: ").split(','))
            array = [int(n) for n in array]
            # Determine a minimum value.
            minimum = int(input("Enter lowest search: "))
            # Determine a maximum value.
            maximum = int(input("Enter highest search: "))
            # Says if a Binary Search was successful.
            print("Search Success: "+str(BinarySearch(array, minimum, maximum)))
        except:
            break

