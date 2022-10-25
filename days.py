# today is tuesday, I want to know what day of the week in n days from now

    # dictionary to have number correlated what day of the week
dd = {
    1 : "Monday",
    2 : "Tuesday",
    3 : "Wednesday",
    4 : "Thursday",
    5 : "Friday",
    6 : "Saturday",
    7 : "Sunday"
}

def dayfinder(day, n, w):
    # some /7 math, to find out how many weeks
    unweeks = w * 7
    new_day = (unweeks + n) % 7

    for i in dd:
        if dd[i] == day:
            day_of_week = i

    final_day = day_of_week + new_day 
    
    if final_day > 7:
        final_day = final_day - 7

    if day in dd.values():
        print(dd[final_day])
    else:
        print("false")

    

dayfinder("Monday", 17, 24)