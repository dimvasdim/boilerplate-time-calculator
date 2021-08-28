def add_time(start, duration, day = "day"):
    time = start.split()
    start_hours = int(time[0].split(":")[0])
    start_minutes = int(time[0].split(":")[1])
    if time[1] == "PM":
        start_hours += 12
    added_hours = int(duration.split(":")[0])
    added_minutes = int(duration.split(":")[1])
    hours = start_hours + added_hours
    minutes = start_minutes + added_minutes
    if minutes > 59:
        hours += minutes // 60
        minutes = minutes % 60
    day_offset = 0
    if hours > 23:
        day_offset = hours // 24
        hours = hours % 24
    form = "AM"
    if hours > 12:
        hours = hours - 12
        form = "PM"
    if hours == 12:
        form = "PM"
    if hours == 0:
        hours = 12
    
    new_time = str(hours) + ":"
    if minutes < 10:
        new_time += "0" + str(minutes)
    else:
        new_time += str(minutes)
    new_time += " " + form

    calendar = {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Saturday",
        6: "Sunday"
    }

    if day != "day":
        select = 0
        for count in calendar:
            if calendar[count].lower() == day.lower():
                select = count
        select = (select + day_offset) % 7
        new_time += ", " + calendar[select]


    if day_offset == 1:
        new_time += " (next day)"
    elif day_offset > 1:
        new_time += " (" + str(day_offset) + " days later)"

    return new_time
