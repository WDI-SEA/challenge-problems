# Valid Parentheses
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.


def properBrackets(nput):
    if len(nput) % 2 !=0:
        return False
    
    dict = {
            "{" : "}",
            "[" : "]",
            "(" : ")"
        }
    
    check = []
    for i in nput:
        if i in dict.keys():
            check.append(i)
        else:
            if check == []:
                return False
            a = check.pop()
            if i != dict[a]:
                return False
        return check == []
properBrackets('(sdalfkjalskf)')
    # check string if there is a open bracket there should be a closed bracket
    # dict in string 
    # boolean - true or false

    # check each of the 3 opening brackets to see if there is a closing bracket at the end
        #'{' needs this '}'

    