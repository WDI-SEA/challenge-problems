# Directions:

# Given a string, return the character that is most commonly used in the string.

# Examples:

# maxChar("abcccccccd") === "c"
# maxChar("apple 1231111") === "1"



def commonLetter(string):

    letterCheck = {}
    #iterate over a  string loop to find all the independent letters then to check if it repeats in string
    for i in string:
        # print(i)
        #before loop check empty array
        if i in letterCheck:
            letterCheck[i] += 1
        # if letter is in string += 1 to that letter
        else:  
            letterCheck[i] = 1

        # check all letters from the letters in string [a,b,c, d
        # then count which ones repeat (add count +1)
        # then figure out which count is the highest
        max_occ = max(letterCheck, key = letterCheck.get)
    print(letterCheck)
    print(max_occ)
    
print(commonLetter("abcccccccd"))