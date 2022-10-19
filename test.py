# Directions:

# Given a string, return the character that is most commonly used in the string.

# Examples:

# maxChar("abcccccccd") === "c"
# maxChar("apple 1231111") === "1"

def commonLetter(string):
    # put letters in a list 
    
    #find common letter in a string
    
    #want to check if there is any repetition

    #iterate over a  string loop to find all the independent letters then to check if it repeats in string
    for i in string:
        print(i)

print(commonLetter("abcccccccd"))