# Week 3 - 8) Write a recursive function (pseudocode and code) that removes all
#             vowels from a string s. Input: "beautiful", Output: "btfl".

'''
PSEUDOCODE
----------

REMOVE_VOWELS(s)
    vowels <- "aeiouAEIOU"
    IF s <- ""
        RETURN s
    ELSE IF s[0] IN vowels
        RETURN removeVowels(s[1:])
    RETURN s[0] + removeVowels(s[1:])
'''

def RemoveVowels(string):
    '''Function to remove vowels from a entered string.'''
    # Define all the possible vowels.
    vowels = "aeiouAEIOU"
    # If the first character in the string is in a vowel.
    if string[0] in vowels:
        # Send next value in the string to RemoveVowels function.
        return RemoveVowels(string[1:])
    # Return the remaining character plus the comparison to check if it is a
    # vowel.
    return string[0] + RemoveVowels(string[1:])
        
if __name__ == "__main__":
    while True:
        # User enters a string value.
        string = input("Enter a string: ")
        # If string is empty close program.
        if string == "":
            break
        # Return result of No Vowels.
        print("No Vowels: "+RemoveVowels(string))
