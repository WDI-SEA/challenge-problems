'''
An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

Example: (Input --> Output)

"Dermatoglyphics" --> true "aba" --> false "moOse" --> false (ignore letter case)
'''

def is_isogram(string):
    letter_list = []
    if len(string) == 0:
        return True
    else:
        for letter in string.lower():
            if letter in letter_list:
                return False
            letter_list.append(letter)
    return True