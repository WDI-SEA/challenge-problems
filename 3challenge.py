# Camel Case-er

# take input and convert - or _ to camel case
# iterate over input
    # join each letter to a new string
    # if character is - or _ skip it and capitalize the next letter

def camel_case(input):
    reference_list = ["-", "_"]
    char_list = list(input)
    new_string = ""
    for i, letter in enumerate(char_list):
        if letter in reference_list:
            char_list[i + 1] = char_list[i + 1].upper()
        else:
            new_string += letter

    return new_string

print(camel_case("the-stealth-warrior"))
print(camel_case("The_Stealth_warrior"))