def add_time(start, duration, starting_day=False):
    start_time_split = start.split()
    start_h_to_m = int(start_time_split[0].split(":")[0]) * 60
    start_m = int(start_time_split[0].split(":")[1])
    total_start_m = start_h_to_m + start_m
    start_am_or_pm = start_time_split[1]

    duration_split = duration.split()
    duration_h = int(duration_split[0].split(":")[0])
    duration_h_to_m = duration_h * 60
    duration_m = int(duration_split[0].split(":")[1])
    total_duration_m = duration_h_to_m + duration_m

    half_day_minutes = 12 * 60
    one_day_minutes = 24 * 60
    m_before_am_pm_swap = half_day_minutes - total_start_m

    new_time = ''

    if duration == "0:00":  # test_no_change: return start time if h and m == 0
        new_time += start

    elif duration == "24:00":  # test_twenty_four: return same time, next day
        new_time += start + " (next day)"

    elif total_duration_m > one_day_minutes:  # count nr of days later than one day
        days_count = (total_duration_m + m_before_am_pm_swap) / one_day_minutes
        print("COUNT", days_count)
        nr_of_days = 0
        if days_count > round(days_count):
            nr_of_days = round(days_count) + 1
        else:
            nr_of_days = round(days_count)
        print("DAYS COUNT", nr_of_days)
        am_pm_in_duration_h = (duration_h / 6)
        current_am_pm = start_am_or_pm
        am_pm = ''
        if current_am_pm == "PM" and am_pm_in_duration_h / 12 == 0:
            am_pm += " PM"
        else:
            am_pm += " AM"
        hours = duration_h % nr_of_days
        minutes = 0
        calculate_remain_muns = int(duration_m) + int(start_m)

        if calculate_remain_muns > 60:
            minutes = calculate_remain_muns - 60
        else:
            minutes = calculate_remain_muns

        minutes_str = "0" + str(minutes)
        if hours == 0:
            new_time += "12:" + minutes_str[-2:] + am_pm + " (" + str(nr_of_days) + " days later)"
        else:
            new_time += str(hours) + ":" + minutes_str[-2:] + am_pm + " (" + str(nr_of_days) + " days later)"

    elif start_am_or_pm == "PM" and m_before_am_pm_swap < total_duration_m:
        new_time_hours = int((total_duration_m - m_before_am_pm_swap) / 60)
        #print("new_time_hours", new_time_hours)

        new_time_minutes = (total_duration_m - m_before_am_pm_swap) - new_time_hours * 60
        minutes_str = "0" + str(new_time_minutes)
        #print("New_time_minutes", minutes_str)

        new_time += str(int(new_time_hours)) + ":" + minutes_str[-2:] + " AM (next day)"

    elif start_am_or_pm == "AM" and (total_duration_m - m_before_am_pm_swap) < 60:
        new_time_minutes = int(total_duration_m - m_before_am_pm_swap)
        if len(str(new_time_minutes)) != 2:
            new_time += "12" + ":0" + str(new_time_minutes) + " PM"
        else:
            new_time += "12" + ":" + str(new_time_minutes) + " PM"

    elif start_am_or_pm == "AM" and m_before_am_pm_swap < total_duration_m:

        new_time_hours = int((total_duration_m - m_before_am_pm_swap) / 60)
        #print("AM HOURS", new_time_hours)
        new_time_minutes = (total_duration_m - m_before_am_pm_swap) - new_time_hours * 60

        if len(str(new_time_minutes)) != 2:
            #print("AM MINUTES", new_time_minutes)
            new_time += str(int(new_time_hours)) + ":0" + str(new_time_minutes) + " PM"
        else:
            new_time += str(int(new_time_hours)) + ":" + str(new_time_minutes) + " PM"

    elif start_am_or_pm == "PM" and m_before_am_pm_swap > total_duration_m:
        total_minutes = int((total_duration_m + total_start_m))
        new_time_hours = int(total_minutes / 60)
        #print(new_time_hours)
        new_time_minutes = int(start_time_split[0].split(":")[1]) + int(duration_m)
        #print(new_time_minutes)
        new_time += str(new_time_hours) + ":" + str(new_time_minutes) + " PM"







    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "Monday", "Tuesday",
                "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    if starting_day and "(next day)" in new_time:
        starting_day_norm = starting_day.lower().capitalize()
        post_day = weekdays[weekdays.index(starting_day_norm) + 1]
        updated_new_time = new_time.split("(")[0].rstrip() + ", " + post_day + " (" + new_time.split("(")[1]
        return updated_new_time

    elif starting_day and "days later" in new_time:
        starting_day_norm = starting_day.lower().capitalize()
        days_max_weeks = nr_of_days - (int(nr_of_days / 7)) * 7
        #print("test", days_max_weeks)
        post_day = weekdays[weekdays.index(starting_day_norm) + days_max_weeks]
        updated_new_time = new_time.split("(")[0].rstrip() + ", " + post_day + " (" + new_time.split("(")[1]
        #print(updated_new_time)
        return updated_new_time

    elif starting_day:
        starting_day_norm = starting_day.lower().capitalize()
        #print(new_time + ", " + starting_day_norm)
        return new_time + ", " + starting_day_norm

    else:
        return new_time
