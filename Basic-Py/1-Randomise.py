# Week 1 - 1) Write a function that randomly shuffles the array of integers and
#             explain the rationale behind its implementation.

# Sets the imports in which the program uses.
from random import *

def Randomise(array):
    ''' Randomises the elements in a passed list.'''
    # Set random list in which to append.
    randomArray = []
    
    while len(array) != 0:

        # Generate a random number between 0 and length of array.
        randomInt = randint(0, len(array)-1)

        # Appends the value of the index randomInt in array to randomList
        randomArray.append(array[randomInt])

        # Remove the value that was selected from the array.
        array.remove(array[randomInt])

    return randomArray

if __name__ == "__main__":
    while True:
        try:
            # Create an array from the users input based off of a comma.
            array = input("Enter an array (seperate by a ','): ").split(",")

            # Converts all values in the array to integers.
            array = [int(n) for n in array]

            # Outputs the returned value from Randomise.
            print(Randomise(array))
        except:
            break

'''
Explain the Rationale behind its implementation.
------------------------------------------------
This could be implemented in generating a collection of dice rolls, or generate a
random order in which people are placed in a competition with the first index
representing first place.
'''
