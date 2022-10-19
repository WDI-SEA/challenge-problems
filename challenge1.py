# Write a program that prints the day of the week given a number of days and weeks.

# Example: 30 days from Monday is Wednesday.

# Answer the following questions:

# Today is Sunday - What day of the week will it be in 100 days?
# Today is Tuesday - What day of the week will it be in 4 weeks and 2 days?
# Today is Friday - What day of the week will it be in 294 days?
# Bonus: What month and day is it 73 days after October 31st 2018?


def what_day(today, days, weeks, remainder=None):
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
    elif today.lower() == 'sunday':
        days += 7
    if int(weeks) != 0:
        days += (int(weeks)*7)
    remainder = int(days) % 7
    if remainder == 1:
        print(f'Your request day will be a Monday')
    elif remainder == 2:
        print(f'Your request day will be a Tuesday')
    elif remainder == 3:
        print(f'Your request day will be a Wednesday')
    elif remainder == 4:
        print(f'Your request day will be a Thursday')
    elif remainder == 5:
        print(f'Your request day will be a Friday')
    elif remainder == 6:
        print(f'Your request day will be a Saturday')
    elif remainder == 0:
        print(f'Your request day will be a Sunday')


todays_input = input('What day of the week is it? \n')
days_input = int(input('How many days in the future? \n'))
weeks_input = int(input('How many weeks in the future? \n'))

what_day(todays_input, days_input, weeks_input)
