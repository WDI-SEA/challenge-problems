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