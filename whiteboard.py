# Given an integer n, return a string array answer (1-indexed) where:
# answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# answer[i] == "Fizz" if i is divisible by 3.
# answer[i] == "Buzz" if i is divisible by 5.
# answer[i] == i (as a string) if none of the above conditions are true.

# integer = int(input("provide a number: \n"))
def fizzbuzz(integer):
    answer = "FizzBuzz"
    # if divisible by 3 and 5
    if integer % 3 == 0 and integer % 5 == 0:
        return print(answer)
    # elif divisible by 3
    elif integer % 3 == 0:
        return print(answer[0:4:])
    # elif divisible by 5
    elif integer % 5 == 0:
        return print(answer[4::])
    # all else
    else:
        return print(f"{integer}")


# fizzbuzz(integer)

# function that returns number of vowels used in a string

input = input('string to count vowels: \n')

def count_vowels(input, output=0):
    vowels = "aeiouAEIOU"
    # iterate string and test if vowel and count up
    for char in input:
        for vowel in vowels:
            if char == vowel:
                output += 1

    return print(output)

# count_vowels(input) 

def count_vowels2(input, output=0):
    vowels = set("aeiouAEIOU")
    # iterate string and test if vowel and count up
    for char in input:
        if char in vowels:
            output += 1

    return print(output)

# count_vowels2(input) 