# Directions:

# Write a function that returns the number of vowels used in a string. Vowels are the characters 'a', 'e'

# Example:


vowels('Hi There!') --> 3
vowels('Why do you ask?') --> 4
vowels('Why?') --> 0



def Check_Vow(string, vowels):

    # The term "casefold" has been used to refer to a method of ignoring cases.

    string = string.casefold()

    count = {}.fromkeys(vowels, 0)

    # To count the vowels

    for character in string:

        if character in count:

            count[character] += 1   

    return count

# Driver Code

vowels = 'aeiou'

string = "Hi, I love eating ice cream and junk food"

print (Check_Vow(string, vowels))

Output: 

{'a': 3, 'e':3 , 'i':2 , 'o':3 , 'u':1}