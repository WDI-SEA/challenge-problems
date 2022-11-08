# Complete a method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case).

# Examples
# "the-stealth-warrior" gets converted to "theStealthWarrior"
# "The_Stealth_Warrior" gets converted to "TheStealthWarrior"


input = "the_stealth-warrior-test--this"

def camelCase_converter(input):
    # make characters into list items
    char_list = list(input)
    for i in range(len(char_list)-1):
        # capitalizing next index when - or _ is encountered
        if char_list[i] == '-' or char_list[i] == '_':
            if char_list[i+1]:
                to_cap = char_list[i+1]
                upper = to_cap.title()
                char_list[i+1] = upper        
    
    # put it back to string
    allString = "".join(char_list)
    output= ""
    # only output characters without - or _
    for char in allString:
        if char != '-' and char != '_':
            output += char
    return output





print(camelCase_converter(input))
