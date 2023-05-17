'''
# 1 - Most efficient way to guess a random number in a range:
 You are given a range of values, and you must write an algorithm to guess a random number in the range in the most efficient way possible.
 After every time you guess, you're told if you're right, too high, or too low.
 '''
def binary_search(arr, target):
    # start with the lowest index for the search
    low = 0
    # start with the highest end of the range for our search
    high = len(arr) - 1

    # iterate through the array while lower index is still less than high index
    while low <= high:
        # find the mid index of the portion between low & high indices
        mid = low + (high - low) // 2
        # save guess to variable to check
        guess = arr[mid]

        # check guess against target
        if guess == target:
            return mid
        # if guess was too low, adjust lower bound to be higher than mid
        elif guess < target:
            low = mid + 1
        # if guess was too high, adjust higher bound to be lower than mid
        else:
            high = mid - 1
    
    # if we finished iterating without answer, it's not there
    return None

arr = [1,2,3,4,5,6,7,8,9]
print("solve 1: ", binary_search(arr, 8))


'''
# 2 - Write an algorithm to flatten a multi-dimensional array:
vec = [[1,2,3], [4,5,6], [7,8,9]] => [1,2,3,4,5,6,7,8,9]
'''
def two_d_flatten(arr):
    # start with new empty array
    flat_arr = []
    # Outer loop to iterate through the outer array
    for sub_arr in arr:
        # inner loop to iterate through each ele in array
        for ele in sub_arr:
            # add each ele to empty array
            flat_arr.append(ele)

    # return new array
    return flat_arr

vec = [[1,2,3], [4,5,6], [7,8,9]]
print("solve 2: ", two_d_flatten(vec))


'''
# 3 -- Write a program that prints the day of the week given a number of days and weeks.
For example: 30 days from Monday is Wednesday.

Answer the following:
'''

def day_of_the_week(day, days_later, weeks_later):
    # check if weeks_later, then convert it to days change
    if weeks_later > 0:
        days_later += (7 * weeks_later)
    #represent the days of the week as an arr
    days = ["sunday","monday", "tuesday", "wednesday", "thursday","friday","saturday"]
    # find the index of the day
    day_index = days.index(day.lower())
    # calculate the new day index
    new_day_index = (days_later + day_index) % 7
    # return days[new day index]
    return days[new_day_index]

#  Today is Sunday - what day of the week will it be in 100 days?
print("solve 3.1: ", day_of_the_week("Monday", 100, 0))
#  Today is Tuesday - What day of the week will it be in 4 weeks and 2 days?
print("solve 3.2: ", day_of_the_week("TUESDAY", 2, 4))
#  Today is Friday - What day of the week will it be in 294 days?
print("solve 3.3: ", day_of_the_week("friday", 294, 0))

#  Bonus: What month and day is it 73 days after October 31st 2018
from datetime import datetime, timedelta
def add_days(start_date, days_to_add):
    # parse the start date into a datetime object
    start_date = datetime.strptime(start_date, "%B %d %Y")
    # calculate new date
    new_date = start_date + timedelta(days=days_to_add)
    # return the new date as a string w/ m, d, y
    return new_date.strftime("%m %d, %Y")
print("solve 3.bonus: ", add_days("October 31 2018", 73))

'''
# 4 -- Given a string, return a new string with the reversed order of characters
reverse('apple') === 'leppa'
reverse('hello') === 'olleh'
reverse('Greetings!') === '!sgniteerG'
'''
def reverse(str):
    return ''.join(reversed(str))

print("solve 4: ", reverse('Greetings!'))


'''
# 5 -- Given a string, return true if the string is a palindrome or false if it is not. Do include spaces and punctuation in determining if the string is a palindrome.
palindrome("abba") === true
palindrome("abcdefg") === false
'''
def is_palindrome(str):
    reversed_str = ''.join(reversed(str))
    if str.lower() == reversed_str.lower():
        return True
    else:
        return False
    
print("solve 5: ", is_palindrome("Abba"))

'''
# 6 -- Given a string, return the character that is most commonly used in the string
maxChar("abcccccccd") === "c"
maxChar("apple 1231111") === "1"
'''
def most_char(str):
    char_dict = {}
    for char in str:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    # find the key with the max value in char_dict
    max_char = max(char_dict, key=char_dict.get)
    return max_char

print("solve 6: ", most_char("abbbbbcccccccd"))


'''
# 7 -- Given an array and chunk size, divide the array into many subarrays where each subarray is of length size
chunk([1, 2, 3, 4], 2) --> [[ 1, 2], [3, 4]]
chunk([1, 2, 3, 4, 5], 2) --> [[ 1, 2], [3, 4], [5]]
chunk([1, 2, 3, 4, 5, 6, 7, 8], 3) --> [[ 1, 2, 3], [4, 5, 6], [7, 8]]
chunk([1, 2, 3, 4, 5], 4) --> [[ 1, 2, 3, 4], [5]]
chunk([1, 2, 3, 4, 5], 10) --> [[ 1, 2, 3, 4, 5]]
'''