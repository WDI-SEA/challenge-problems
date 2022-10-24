# Challenges

this is a list of easy - medium coding challenges in no partiuclar order

---

Most effecient way to guess a random number in a range:

You are given a range of values, and you must write an algorithm to guess a random number in the range in the most effecient way possible.

After every time you guess, you're told if you're right, too high, or too low.

---

Write an algorithm to flatten a multi-dimensional array:

```
vec = [[1,2,3], [4,5,6], [7,8,9]]
=> [1,2,3,4,5,6,7,8,9]
```
---

Write a program that prints the day of the week given a number of days and weeks.

Example: 30 days from Monday is Wednesday.

Answer the following questions:

* Today is Sunday - What day of the week will it be in 100 days?
* Today is Tuesday - What day of the week will it be in 4 weeks and 2 days?
* Today is Friday - What day of the week will it be in 294 days?
* Bonus: What month and day is it 73 days after October 31st 2018?

---

Directions:
Given a string, return a new string with the reversed
order of characters

Examples

```
reverse('apple') === 'leppa'
reverse('hello') === 'olleh'
reverse('Greetings!') === '!sgniteerG'
```

---

Directions:
Given a string, return true if the string is a palindrome
or false if it is not. Palindromes are strings that
form the same word if it is reversed. Do include spaces
and punctuation in determining if the string is a palindrome.

Examples:

```
palindrome("abba") === true
palindrome("abcdefg") === false
```

---

Directions:

Given a string, return the character that is most
commonly used in the string.

Examples:

```
maxChar("abcccccccd") === "c"
maxChar("apple 1231111") === "1"
```

---

Directions:
Given an array and chunk size, divide the array into many subarrays
where each subarray is of length size

Examples:

```
chunk([1, 2, 3, 4], 2) --> [[ 1, 2], [3, 4]]
chunk([1, 2, 3, 4, 5], 2) --> [[ 1, 2], [3, 4], [5]]
chunk([1, 2, 3, 4, 5, 6, 7, 8], 3) --> [[ 1, 2, 3], [4, 5, 6], [7, 8]]
chunk([1, 2, 3, 4, 5], 4) --> [[ 1, 2, 3, 4], [5]]
chunk([1, 2, 3, 4, 5], 10) --> [[ 1, 2, 3, 4, 5]]
```

---

Direction:

Given an amount of change, determine the minimum number of coins required to make that change

Examples:

```
greedy(65) --> 4 `(2 quarters, 1 dime, 1 nickle)`
greedy(5) --> 1 `(1 nickle)`
```

---

Directions:

Given an integer (either positive or negative), reverse the number and keep it's sign.

Example:

```
reverseInt(-51) --> -15
reverseInt(100) --> 001 --> 1
reverseInt(601) --> 106
```

---

Directions:

Write a function that returns the number of vowels used in a string. Vowels are the characters 'a', 'e'

Example:

```
vowels('Hi There!') --> 3
vowels('Why do you ask?') --> 4
vowels('Why?') --> 0
```

--- 

reverse an array in place (in place means do not make a new array in order to reverse given array) without using builtin method for reversal (example not `.reverse` in python)

---

implement a forEach (a function that works like Array.forEach() -- accepts a callback and invokes it on every element in an array)

---

Given an array of integers, find the one that appears an odd number of times

---

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

Bonus: solve recursively

---

Write a function that takes in a list of numbers and gives you back a tuple or list with two items: the sum of all negative numbers in the list, and the count of all positive numbers.

For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65]. (There are 10 positive numbers, and the negative numbers add up to -65.)

---

Implement a function unique_in_order that will take in an argument either a string or an array and return a list of elements without any elements with the same # values next to each other, but preserving the original order.

```
unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1,2,2,3,3])       == [1,2,3]
```
---

Given an array of integers as strings and numbers, return the sum of the array values as if all were numbers.

Return your answer as a number.

---

Complete a method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case).

```
Examples
"the-stealth-warrior" gets converted to "theStealthWarrior"
"The_Stealth_Warrior" gets converted to "TheStealthWarrior"
```

---

Given an array of integers, find the one that appears an odd number of times.

There will always be only one integer that appears an odd number of times.

---

Complete the solution so that it splits the string into pairs of two characters.
If the string contains an odd number of characters then it should replace the  missing second character of the final pair with an underscore ('_').

---

given an array and a total, return true if one or more consecutive numbers in the array sum up to that total

---

Write a function that takes an array as a parameter and returns an array with the elements in a random order.

---


