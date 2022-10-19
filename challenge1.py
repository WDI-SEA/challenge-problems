# Leetcode- Medium

# 17. Letter Combinations of a Phone Number

# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

digits = input("provide up to two digit number between (2 - 9) for letter combinations: \n")
def letterCombinations(digits, output = []):
    num_letters = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
    }

    if len(digits) == 0:
        return output
    elif len(digits) == 1:
        for letter in num_letters[digits]:
            output.append(letter)
    else:
        list = []
        for i in range(0, len(digits)):
            list.append(num_letters[digits[i]])
        
        combined = [[f,s] for f in list[0] for s in list[1]]

        for arr in combined:
            output.append("".join(arr))

    return print(output)

letterCombinations(digits)



        