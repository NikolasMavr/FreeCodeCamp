def add_time(start, duration, day_of_week=False):
    days_of_the_week_index = {"monday": 0, "tuesday": 1, "wednesday": 2,
                              "thursday": 3, "friday": 4, "saturday": 5, "sunday": 6}
    days_of_the_week_array = ["Monday", "Tuesday", "Wednesday", "Thursday",
                              "Friday", "Saturday", "Sunday"]

    start_hour = int(start.split()[0].split(':')[0])
    start_minutes = int(start.split()[0].split(':')[1])
    am_pm = start.split()[1]
    am_pm_flip = {"AM": "PM", "PM": "AM"}

    duration_hour = int(duration.split(":")[0])
    duration_minutes = int(duration.split(":")[1])

    new_time_hour = (start_hour + duration_hour) % 12
    new_time_minutes = start_minutes + duration_minutes

    amount_of_days = int(duration_hour / 24)

    if new_time_minutes >= 60:
        new_time_hour += 1
        start_hour += 1
        new_time_minutes = new_time_minutes % 60

    amount_of_am_pm_flips = int((start_hour + duration_hour) / 12)
    new_time_minutes = new_time_minutes if new_time_minutes > 9 else "0" + str(new_time_minutes)

    if am_pm == "PM" and start_hour + (duration_hour % 12) >= 12:
        amount_of_days += 1

    if new_time_hour > 12:
        new_time_hour = new_time_hour % 12
        if new_time_hour == 0:
            new_time_hour += 1
        if am_pm == 'PM':
            amount_of_days += 1

    am_pm = am_pm_flip[am_pm] if amount_of_am_pm_flips % 2 == 1 else am_pm
    new_time = str(new_time_hour) + ":" + str(new_time_minutes) + " " + am_pm

    if day_of_week:
        day_of_week = day_of_week.lower()
        index = int((days_of_the_week_index[day_of_week]) + amount_of_days) % 7
        new_day = days_of_the_week_array[index]
        new_time += ", " + new_day

    if amount_of_days == 1:
        return new_time + " " + "(next day)"
    elif amount_of_days > 1:
        return new_time + " (" + str(amount_of_days) + " days later)"

    return new_time


print(add_time("11:59 PM", "24:05", "Monday"))
