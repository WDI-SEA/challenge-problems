# Camel Case-er

# take input and convert - or _ to camel case
# iterate over input
    # join each letter to a new string
    # if character is - or _ skip it and capitalize the next letter

def camel_case(input):
    # list for reference
    reference_list = ["-", "_"]
    # convert input into list of characters in input
    char_list = list(input)
    # initialize our new string
    new_string = ""
    # iterate over our list of characters
    for i, letter in enumerate(char_list):
        # if that character is a - or _
        if letter in reference_list:
            # upper case the next character
            char_list[i + 1] = char_list[i + 1].upper()
        # add all other characters to our new string
        else:
            new_string += letter

    return new_string

print(camel_case("the-stealth-warrior"))
print(camel_case("The_Stealth_warrior"))

# bonus -- do the reverse
# take camel cased input and return underscores
def underscorerer(input):
    # convert input to list of characters
    char_list = list(input)
    # empty list to append characters (python will hang if I try to insert into a list while looping over it)
    new_char_list = list()
    # iterate over character list
    for i, char in enumerate(char_list):
        # make sure our first letter is lower cased and don't add anything before it
        if i == 0:
            char = char.lower()
        # if the character is uppercased
        elif char.isupper():
            # convert it to lower case
            char = char.lower()
            # append an underscore to our new list before the character
            new_char_list.append("_")
        # append each character to our new list
        new_char_list.append(char)

    # return a stringified version of our list
    return "".join(new_char_list)

print(underscorerer("myCamelCasedVariable"))
print(underscorerer("ThisOneIsPascalCased"))