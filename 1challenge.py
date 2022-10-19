## Days of the Week

# list with all the days of the week
# 1 week = 7 days
# add the total days and weeks given to number assigned to given day
# divide total by 7 and determine remainder
# remainder should equal index of that day

def what_day_is_it(day: str, num_days = 0, num_weeks = 0):
    # days of the week list
    days_of_the_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    # calculate the total number of days given
    total_num_days = num_days + (num_weeks * 7)
    # check that given day is real and handle any mismatched casing
    capitalized_day = day.capitalize()
    if capitalized_day in days_of_the_week:
        # using day's index as reference add the number of days given
        total = days_of_the_week.index(capitalized_day) + total_num_days
        # divide 
        new_day = total % 7
        print(f"The day will be {days_of_the_week[new_day].capitalize()}")
    else:
        print("Error. Please enter a day of the week")
        print("It's spelled Wednesday")

what_day_is_it("mOndAY", 30)
what_day_is_it("Sunday", 100)
what_day_is_it("Tuesday", 2, 4)
what_day_is_it("Friday", 294)