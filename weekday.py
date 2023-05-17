print("What day is it?")
day = input("> ")

print("How many days from today?")
duration = input("> ")

week = {
    "monday": 0,
    "tuesday": 1,
    "wednesday": 2,
    "thursday": 3,
    "friday": 4,
    "saturday": 5,
    "sunday": 6
}

week_arr = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

remainder = (week[day] + int(duration)) % 7
print(week_arr[remainder])

