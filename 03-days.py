'''

Write a program that prints the day of the week given a number of days and weeks.

Example: 30 days from Monday is Wednesday.

Answer the following questions:

* Today is Sunday - What day of the week will it be in 100 days?
* Today is Tuesday - What day of the week will it be in 4 weeks and 2 days?
* Today is Friday - What day of the week will it be in 294 days?
* Bonus: What month and day is it 73 days after October 31st 2018?

'''


def weekday(beginning_day, add_days):
    weekdays = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
    index = int(weekdays.index(beginning_day)) 
    days = add_days % 7
    index2 = (index + days) % 7
    return weekdays[index2]

print(weekday("saturday", 5))