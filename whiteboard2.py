# A pangram is a sentence where every letter of the English alphabet appears at least once.
# Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.
# Example 1:
# Input: sentence = “thequickbrownfoxjumpsoverthelazydog”
# Output: true
# Explanation: sentence contains at least one of every letter of the English alphabet.
# Example 2:
# Input: sentence = “leetcode”
# Output: false

string = 'awkiefhjslkjhtergyjawl wlkjflskjfjliwewlilsjf'

def pangram_check(string):
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    alphabets_list = list(alphabets)

    if len(string) < 26:
        return False
    
    for char in string:
        if char in alphabets_list:
            alphabets_list.remove(char)
            # print(alphabets_list)
    
    if len(alphabets_list) > 0:
        return False
    else:
        return True

print(pangram_check(string))



