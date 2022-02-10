def add_time(start, duration, starting_day=False):
    start_time_split = start.split()
    start_h = int(start_time_split[0].split(":")[0])
    start_h_to_m = int(start_time_split[0].split(":")[0]) * 60
    start_m = int(start_time_split[0].split(":")[1])
    total_start_m = start_h_to_m + start_m
    start_am_or_pm = start_time_split[1]

    duration_split = duration.split()
    duration_h = int(duration_split[0].split(":")[0])
    duration_h_to_m = duration_h * 60
    duration_m = int(duration_split[0].split(":")[1])
    total_duration_m = duration_h_to_m + duration_m

    end_minutes = start_m + duration_m
    if end_minutes >= 60:
        start_h += 1
        end_minutes = end_minutes % 60

    # TODO: I do not understand
    nr_hours = (start_h + duration_h) % 12
    end_hours = ''
    if nr_hours == 0:
        end_hours += str(12)
    else:
        end_hours += str(nr_hours)

    # calculate when to swap AM and PM
    # sum up the start and duration hours and / 12
    nr_of_am_pm_swaps = int((start_h + duration_h) / 12)
    print("nr_of_am_pm_swaps", nr_of_am_pm_swaps)

    # TODO: I do not understand
    am_pm = ''
    if start_am_or_pm == "PM" and nr_of_am_pm_swaps % 2 == 1:
        am_pm += " AM"
    else:
        am_pm += " PM"

    # TODO: I do not understand
    # find out if duration hours contain days
    nr_of_days = int(duration_h / 24)
    if start_am_or_pm == "PM" and start_h + (duration_h % 12) >= 12:
        nr_of_days += 1
    print("NR_of_days", nr_of_days)

    if duration == "0:00":
        new_time = start
    elif duration == "24:00":
        new_time = start + " (next day)"
    elif nr_of_days == 1:
        new_time = end_hours + ":" + ("0" + str(end_minutes))[-2:] + am_pm + " (next day)"
        print(new_time)
    elif nr_of_days > 1:
        new_time = end_hours + ":" + ("0" + str(end_minutes))[-2:] + am_pm + " (" + str(nr_of_days) + " days later)"
        print(new_time)
    else:
        new_time = end_hours + ":" + ("0" + str(end_minutes))[-2:] + am_pm
        print(new_time)

    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    if starting_day and "next day" in new_time:
        starting_day_norm = starting_day.lower().capitalize()
        post_day = weekdays[weekdays.index(starting_day_norm) + 1]
        part = new_time.split("(")[1].rstrip()
        print(part)
        new_time = new_time.split("(")[0].rstrip() + ", " + post_day + " (next day)"






    # elif starting_day and "days later" in new_time:
    #     starting_day_norm = starting_day.lower().capitalize()
    #     if weekdays[weekdays.index(starting_day_norm) + nr_of_days < 7:
    #         post_day = weekdays[weekdays.index(starting_day_norm) + days_max_weeks]
    #         new_time = new_time.split("(")[0].rstrip() + ", " + post_day + " (" + new_time.split("(")[1])
    #

        # days_max_weeks = nr_of_days - (int(nr_of_days / 7)) * 7
        # #print("test", days_max_weeks)
        # post_day = weekdays[weekdays.index(starting_day_norm) + days_max_weeks]


    # if starting_day:
    #     starting_day_norm = starting_day.lower().capitalize()
    #     new_time = new_time + ", " + starting_day_norm
    # else:
    #     starting_day_norm = starting_day.lower().capitalize()
    #     new_time = new_time + ", " + starting_day_norm
    print(new_time)
    return new_time





    # elif starting_day and "days later" in new_time:
    #     starting_day_norm = starting_day.lower().capitalize()
    #     days_max_weeks = nr_of_days - (int(nr_of_days / 7)) * 7
    #     #print("test", days_max_weeks)
    #     post_day = weekdays[weekdays.index(starting_day_norm) + days_max_weeks]
    #     updated_new_time = new_time.split("(")[0].rstrip() + ", " + post_day + " (" + new_time.split("(")[1]
    #     #print(updated_new_time)
    #     return updated_new_time
    #
    # elif starting_day:
    #     starting_day_norm = starting_day.lower().capitalize()
    #     #print(new_time + ", " + starting_day_norm)
    #     return new_time + ", " + starting_day_norm
    #
    # else:
    #     return new_time
