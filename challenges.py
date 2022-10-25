# Write a function that returns the number of vowels used in a string. Vowels are the characters 'a', 'e'

# Example:

# vowels('Hi There!') --> 3
# vowels('Why do you ask?') --> 4
# vowels('Why?') --> 0

# string =input("enter your phrase: \n")

def vowels(string):
    #  define vowels using set{} -. set stores  multiple items into a single variable
    vowels = set("aeiouAEIOU")
    # init the vowel count at zero
    count = 0
    #  iterate through the string
    for letters in string:
    # if vowel is found return vowel+1
        if letters in vowels:
            count = count +1
    print("No of vowels :", count)

# vowels(string)



# Given an integer n, return a string array answer (1-indexed) where:

# answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# answer[i] == "Fizz" if i is divisible by 3.
# answer[i] == "Buzz" if i is divisible by 5.
# answer[i] == i (as a string) if none of the above conditions are true.

num = int(input("choose a number \n"))
def fizzbizz(num):
    # if num is div by 3 and 5 
    if num % 3 == 0 and num % 5 == 0:
    # return fizzbizz
        print("fizzbizz")
    #  if num div by 3 
    elif num % 3 == 0:
    #  return fizz
        print("fizz")
    #  if num div by 5
    elif num % 5 == 0:
        print ("bizz")
    else:
        print("number is not divisble by 3 or 5 boo")

fizzbizz(num)



# From Git-repo

# Direction:
# Given an amount of change, determine the minimum number of coins required to make that change
# Examples:

# greedy(65) --> 4 `(2 quarters, 1 dime, 1 nickle)`
# greedy(5) --> 1 `(1 nickle)`

num = int(input("enter change amount"))
def change(num):
    # given a number 
    if num == 0:
        return 0
    # if num  > 25 then 
    if num >= 25:
        qtr_results = num //25 #returns how many quarters used
        qtr_remainder = num % 25 # returns what remains 
        return qtr_results
    #  if not then remainder and div that by 10 % ==0 then return answer
    if num >= 10:
    # div by 10
        dime_results = qtr_remainder //10 
        dime_remainder = num % 10
    # if not then dived the rem by 5
    if num >= 5:
    # div by 5
        nickel_results = dime_remainder //5 
        remainder = num % 1 
   