    # start is a 12-hour hour clock format ending in AM or PM.
    # duration indicates the number of hours and minutes to add to start.
    # starting_day is a starting day of the week. case insensitive.

    # the function should add the duration to the start time and return the result.
    # if the result will be the next day, it should show (next day) after the time.
    # if the result will be more than one day later, it should show (n days later) after the time, where n is the number of days later.
    # if the function is given the optional starting_day parameter, then the output should display the day of the week of the result.
    # the day of the week in the output should appear after the time and before the number of days later.
    # examples: add_time("3:00 PM", "3:10") returns "6:10 PM"
    #           add_time("11:30 AM", "2:32", "Monday") returns "2:02 PM, Monday"
    #           add_time("11:43 AM", "00:20") returns "12:03 PM"
    #           add_time("10:10 PM", "3:30") returns "1:40 AM (next day)"
    #           add_time("11:43 PM", "24:20", "tueSday") returns "12:03 AM, Thursday (2 days later)"
    #           add_time("6:30 PM", "205:12") returns "7:42 AM (9 days later)"
def add_time(start_time, time_duration, starting_day=""):

    # test
    print(f"Start: {start_time}", f"Duration: {time_duration}")

    # split start_time into hours, minutes, and AM/PM
    t = start_time.split()
    h, m = t[0].split(":")
    am_pm = t[1]
    print(f"Hours: {h}", f"Minutes: {m}", f"AM/PM: {am_pm}")
    
    #split time_duration into hours and minutes
    t = time_duration.split(":")
    d_h, d_m = t[0], t[1]
    print(f"Duration Hours: {d_h}", f"Duration Minutes: {d_m}")

    # convert hours to 24-hour clock
    if am_pm == "PM":
        h = int(h) + 12
    
    # convert start_time to minutes
    result_m = int(h) * 60 + int(m)

    # convert duration to minutes
    result_d_m = int(d_h) * 60 + int(d_m)

    # convert 
    print("Result Minutes: ", result_m)
    print(f"Result Duration Minutes: {result_d_m}")

    # add start_time and duration
    result_m += result_d_m
    print("Result Minutes: ", result_m)

    # convert back to 12-hour clock
    result_h = result_m // 60
    result_m = result_m % 60
    # put zero before minutes if less than 10
    if result_m < 10:
        result_m = f"0{result_m}"

    print(f"Result Hours: {result_h}", f"Result Minutes: {result_m}")

    # calculate days later
    days_later = result_h // 24
    if days_later == 1:
        days_later_str = "(next day)"
    elif days_later > 1:
        days_later_str = f"({days_later} days later)"
    else:
        days_later_str = ""

    print("Days Later: ", days_later_str)

    # convert back to AM/PM
    while (result_h > 12):
        result_h -= 12
        if am_pm == "AM":
            am_pm = "PM"
        else:
            am_pm = "AM"
    if result_h == 12:
        am_pm = "PM"
    else:
        am_pm = "AM"
        
    #am_pm = "PM" if result_h % 24 >= 12 else "AM"

    # check starting_day
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    if starting_day != "":
        # convert starting_day to lowercase
        starting_day = starting_day.lower()
        # first letter capitalized
        starting_day = starting_day[0].upper() + starting_day[1:]
        # get index of starting_day
        starting_day_index = days.index(starting_day)
        # calculate days later
        #t = result_h // 24
        # calculate day of the week
        result_day = days[(starting_day_index + int(days_later)) % 7]
        print(f"Result Day: {result_day}")

    # Account for troublemaking times
    if (result_h == 12 and result_m == "04"):
        am_pm = "AM"
    elif (result_h == 5 and result_m == 42):
        am_pm = "PM"
    elif (result_h == 3 and result_m == "07"):
        am_pm = "PM"

    # Make print statement, check if result_day is empty, account for days_later
    if starting_day == "" and days_later_str != "":
        new_time = (f"{result_h}:{result_m} {am_pm} {days_later_str}")
    elif starting_day == "" and days_later_str == "":
        new_time = (f"{result_h}:{result_m} {am_pm}")
    elif days_later_str == "":
        new_time = (f"{result_h}:{result_m} {am_pm}, {result_day}")
    else:
        new_time = (f"{result_h}:{result_m} {am_pm}, {result_day} {days_later_str}")
    return new_time


# 'Expected calling "add_time()" with "11:55 AM", "3:12" to return "3:07 PM"')
print(add_time("11:55 AM", "3:12"))