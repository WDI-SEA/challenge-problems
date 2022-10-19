# Most effecient way to guess a random number in a range:
# You are given a range of values, and you must write an algorithm to guess a random number in the range in the most effecient way possible.
# After every time you guess, you're told if you're right, too high, or too low.

# import random
import random
# defining an array
arr = [1,2,3,4,5,6,7,8,9]

# defining a function that takes an input num as a guess
def guess(num):
    # defining a random variable to be one of the numbers in the array
    target = random.choice(arr)
    if (num == target):
        print('you guessed correctly')
    else:
        if (num > target):
            print('too high guess again')
        else:
            print('too low guess again')

# guess(6)


# Write an algorithm to flatten a multi-dimensional array:

# vec = [[1,2,3], [4,5,6], [7,8,9]]
# => [1,2,3,4,5,6,7,8,9]

# for each entry in the array, splice and push into the dictionary as a new item

# create a new array by iterating through the dictionary I created

# import chain from python intertools
from itertools import chain

def flattenArray(arr):
    # chain.from_iterable is a method that takes every singular item from a string or array and puts it as a new item
    newArray = list(chain.from_iterable(arr))
    print(newArray)

# flattenArray([[1,2,3], [5,6], [8,9,0]])


# Write a program that prints the day of the week given a number of days and weeks.

# Example: 30 days from Monday is Wednesday.

# Answer the following questions:

# * Today is Sunday - What day of the week will it be in 100 days?
# * Today is Tuesday - What day of the week will it be in 4 weeks and 2 days?
# * Today is Friday - What day of the week will it be in 294 days?
# * Bonus: What month and day is it 73 days after October 31st 2018?

# week = 7
# day = 1
daysOfWeek = ["Monday", "Tuesday", 'Wednesday', 'Thursday', 'Friday', 'Saturday', "Sunday"]

# do some math to see what index of the days of the week we are at
 
# use % opporator to get a remainder and then have the remainder correspond to a date

def getDay(day, days, weeks):
    # index the days of the week array
    index = daysOfWeek.index(day)
    # create a variable for days/weeks that gives them values
    num = (1 * days) + (7 * weeks)
    newIndex = num % 7
    newDay = newIndex + index
    print(daysOfWeek[newDay])

# getDay('Tuesday', 187, 4)

# Directions:
# Given a string, return a new string with the reversed
# order of characters

# Examples

# reverse('apple') === 'leppa'
# reverse('hello') === 'olleh'
# reverse('Greetings!') === '!sgniteerG'

def reverseWord(string):
    # base case
    if (len(string) == 0):
        return ""
    # return the 
    return string[-1] + reverseWord(string[:-1])

# print(reverseWord('apple'))

# Directions:
# Given a string, return true if the string is a palindrome
# or false if it is not. Palindromes are strings that
# form the same word if it is reversed. Do include spaces
# and punctuation in determining if the string is a palindrome.

# Examples:

# palindrome("abba") === true
# palindrome("abcdefg") === false

def palindrome(string):
    # create a function to reverse the string
    newString = string[::-1]
    # if the string is equal to the newString it is a palindrome
    if newString == string:
        print('palindrome!')
    # otherwise it is not
    else:
        print('not palindrome!')

# palindrome('apple')
# palindrome('racecar')
# palindrome('!racecar!')
# palindrome('r aceca r')

# Directions:

# Given a string, return the character that is most
# commonly used in the string.

# Examples:

# maxChar("abcccccccd") === "c"
# maxChar("apple 1231111") === "1"


def letterCount(word):
    # create a dictonary where I will keep track of the letter count in string 
    count= { }
    # iterate through the string and account for every letter
    for char in word:
        if char in count:
        # if a letter does exist add 1 to the existing count
            count[char] += 1
        # if a letter does not exist, create one and add 1
        else:
            count[char] = 1
        # return the letter with the highest count
    maxChar = max(count, key = count.get)

    return(print(maxChar))

letterCount('apple')
    