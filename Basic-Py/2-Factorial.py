# Week 1 - 2) Count the number of trailing 0s in a factorial number

def Factorial(N):
    ''' Calculates the number of trailing zeros in a factorial. '''

    # Sets noZeros as 0
    noZeros = 0
    factorial = 1
    # Loops in for all the values in range between 1 and the number entered.
    for i in range(1, N):

        # Increments the noZeros by the integer of the number entered divided
        # by 5 to the power.
        noZeros += int(N//(5**i))
        
    return noZeros

if __name__ == "__main__":
    while True:
        try:
            # Allows user to enter a numerical value.
            number = int(input("Enter a number: "))

            # Returns the number of trailing 0s the factorial will have.
            print("Number of Trailing 0s: "+str(Factorial(number)))
        except:
            break
