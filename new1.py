# Write a program that prints the day of the week given a number of days and weeks.

# Example: 30 days from Monday is Wednesday.

# Answer the following questions:

# * Today is Sunday - What day of the week will it be in 100 days?
# * Today is Tuesday - What day of the week will it be in 4 weeks and 2 days?
# * Today is Friday - What day of the week will it be in 294 days?

# create an array from 0-6 for the 7 days of the week


class Solution:
     def daysOfTheWeek(d):
          calendar = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
          # w = 7
          # d = 1
          # w = input("how many weeks? please enter an integer\n")
          # return w
          
          d = input("how many days? please enter an integer\n")

          i = int(d)

          for i in calendar:
               print(i)

     daysOfTheWeek(0, 100)



# accept a user input (integer) for amount of days to look down the calender

# take user input and iterate across the array in a loop for the amount of days specified