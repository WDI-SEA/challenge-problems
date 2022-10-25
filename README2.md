# Write a program that prints the day of the week given a number of days and weeks.

# Example: 30 days from Monday is Wednesday.

# Answer the following questions:

# Today is Sunday - What day of the week will it be in 100 days?
# Today is Tuesday - What day of the week will it be in 4 weeks and 2 days?
# Today is Friday - What day of the week will it be in 294 days?
# Bonus: What month and day is it 73 days after October 31st 2018?

1. Sunday
2. Monday
3. Tues
4. Wed
5. Thu.
6. Fri.
7. Sat

5

30 days it the goal

7 * 4 = 28, remainder 2 days. 2 days from Monday is Wed
Monday 

    if 
    days % 7 = remainder

    if remainder 1

def date (today,day,weeks)
  if today.lower() == 'monday':
        days += 1
    elif today.lower() == 'tuesday':
        days += 2
    elif today.lower() == 'wednesday':
        days += 3
    elif today.lower() == 'thursday':
        days += 4
    elif today.lower() == 'friday':
        days += 5
    elif today.lower() == 'saturday':
        days += 6
    
    days += (weeks*7)
    remainder = days % 7

    if remainder == 1
        print('The day of the week will be Monday')



