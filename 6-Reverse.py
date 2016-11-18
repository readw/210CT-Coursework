# Week 3 - 6) Write the pseudocode and code for a function that reverses the
#             words in a sentance. Input: "This is awesome" Output: "awesome
#             this Is". Give the Big O notation.

'''
PSEUDOCODE - ITERATIVE
----------------------
REVERSE_ORDER(s)
    rev <- SPLIT s BY " "
    reversed <- ""
    FOR i IN COUNTDOWN length of rev TO 0
        IF i != 0
            reversed += rev[i]+" "
        ELSE
            reversed += rev[i]
    RETURN reversed

PSEUDOCODE - RECURSIVE
----------------------
REVERSE_ORDER(s, length)
    IF length = 0
        RETURN s[0]
    ELSE
        RETURN REVERSE_ORDER(s[0-length:], length-1) & " " & s[0]
'''

#######################
## Iterative Version ##
#######################
def reverseOrderIter(string):
    '''Iterative Solution that reverses the order of all seperate words within
a passed string.'''
    # Set reversed string as an empty string.
    reversedString = ""

    # Loop through the list in reverse order.
    for i in range(len(string)-1,-1,-1):
        # If it isn't the last value in the array.
        if i != 0:
            # Append reversedString with the value and a space.
            reversedString += string[i]+" "
        # If it is the last value in the array.
        else:
            # Appened reversed String with the word.
            reversedString += string[i]
            
    return reversedString

#######################
## Recursive Version ##
#######################
def reverseOrderRec(sentence, length):
    '''Recursive Solution that reverses the order of all seperate words within
a passed string.'''
    # If the length of the string array is 0.
    if length == 0:
        # Return back the selected value.
        return sentence[0]
    else:
        # Call the function passing the array back and taking 1 from the length.
        return reverseOrderRec(sentence[0-length:], length-1)+" "+sentence[0]

if __name__ == "__main__":
    while True:
        try:
            # User inputs a phrase and it is created into a list.
            sentance = input("Please enter a sentance: ").split(" ")
            # Calls iterative reverse order function.
            print("Result (Iterative): "+reverseOrderIter(sentance))
            # Calls recursive reverse order function.
            print("Result (Recursive): "+reverseOrderRec(sentance,len(sentance)-1))
        except:
            break
