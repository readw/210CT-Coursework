# Week 5 - 10) Given a sequence of n integer numbers, extract the sub-sequence
#              of maximum length which is in ascending order.

'''
PSEUDOCODE
----------
SUB_SEQUENCE(array)
    start <- 0
    maxStart <- 0
    maxLength <- 0
    
    FOR i IN range(length of array - 1)
        IF array[i] > array[i+1]
            IF maxLength < i - start
                maxLength = i - start
                maxStart = start
            start = i + 1
            
    IF maxLength == 0
        RETURN array

    RETURN array[maxStart:(maxStart+maxLength)+1]
'''

def SubSequence(array):
    '''Determines maximum group of numbers that are in ascending order.'''               # Example: n=3
    # Set default values for start, maxStart and maxLength
    start, maxStart, maxLength = 0, 0, 0                                                 # O(1) --> O(1)

    # For each item in the array.
    for i in range(len(array)-1):                                                        # O(n) --> O(3)
        # Compare the value with the next one to see if greater.
        if array[i] > array[i+1]:                                                        # O(n) --> O(3)
            # If maxLength is less than the difference between the start point
            # and the current iteration.
            if maxLength < i - start:                                                    # O(n) --> O(3)
                # Set maxLength to difference of current point and start.
                maxLength = i - start                                                    # O(n) --> O(3)
                # Set maxStart to current start value.
                maxStart = start                                                         # O(n) --> O(3)
            start = i + 1                                                                # O(n) --> O(3)
    # Determine if a maxLength has been defined.
    if maxLength == 0:                                                                   # O(1) --> O(1)
        return array                                                                     # O(1) --> O(1)
    # Return the specific value of the array.
    return array[maxStart:(maxStart+maxLength+1)]                                        # O(1) --> O(1)

if __name__ == "__main__":
    while True:
        try:
            # User enters a value integer array.
            array = input("Enter a list of integers (seperated by ','): ").split(",")
            array = [int(n) for n in array]
            # Output the SubSequence
            print("Sub Sequence: "+str(SubSequence(array)))
        except:
            break
