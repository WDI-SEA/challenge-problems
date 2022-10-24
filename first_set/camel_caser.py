# Complete a method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case).

# Examples
# "the-stealth-warrior" gets converted to "theStealthWarrior"
# "The_Stealth_Warrior" gets converted to "TheStealthWarrior"

import re

testWord1 = 'the-stealth-warrior'
testWord2 = 'The_stealth_Warrior'

def regexKek(word):
    newWord = re.findall('[A-Za-z0-9]+', word)
    if (word[0][0] == ''.join(re.findall('[A-Z]', newWord[0]))):
        for i in range(len(newWord)):
            newWord[i] = newWord[i].capitalize()
    else:
        for i in range(1, len(newWord)):
            newWord[i] = newWord[i].capitalize()

    return ''.join(newWord)

print(regexKek(testWord1))