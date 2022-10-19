# Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.


function even_or_odd(number) {
  if (number%2 == 0) {
    return "Even";
  } else {
    return "Odd";
  }
}

//Using the modulus operator, can check if number is divisible by 2 to find all even values

//Can also refactor this function using a ternary operator below for better performance.

function even_or_odd(number) {
  return number % 2 == 0 ? "Even" : "Odd"
}


https://leetcode.com/problems/longest-palindromic-substring/

Given a string s, return the longest palindromic substring in s.

A string is called a palindrome string if the reverse of that string is the same as the original string.

