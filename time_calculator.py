def add_time(start, duration, starting_day=False):
    total_am_pm_minutes = 12 * 60
    print("total_am_pm_minutes", total_am_pm_minutes)
    start_time_split = start.split()
    start_h_to_minutes = int(start_time_split[0].split(":")[0]) * 60

    start_time_minutes = int(start_time_split[0].split(":")[1])
    start_time_to_minutes = start_h_to_minutes + int(start_time_split[0].split(":")[1])
    print("start_time_to_minutes", start_time_to_minutes)
    time_till_am_pm_swap = total_am_pm_minutes - start_time_to_minutes
    print("time_till_am_pm_swap", time_till_am_pm_swap)

    duration_split = duration.split()
    duration_hours = int(duration_split[0].split(":")[0])
    duration_h_to_minutes = duration_hours * 60
    duration_minutes = (duration_split[0].split(":")[1])
    print("duration_minutes", duration_minutes)
    # print("duration hours, duration_h_to_minutes", duration_hours, duration_h_to_minutes)
    total_duration_minutes = int(duration_h_to_minutes) + int(duration_minutes)
    print("total_duration_minutes", total_duration_minutes)
    # minutes_sum = int(start_time_to_minutes) + int(duration_minutes)

    new_time = ''
    one_day_minutes = 24 * 60

    if duration == "0:00":
        new_time += start

    elif duration == "24:00":
        new_time += start + " (next day)"

    elif total_duration_minutes > one_day_minutes:
        # nr of days later
        days_count = (total_duration_minutes + time_till_am_pm_swap) / one_day_minutes
        nr_of_days = 0
        if days_count > round(days_count):
            nr_of_days = round(days_count) + 1
        else:
            nr_of_days = round(days_count)
        print("DAYS COUNT", nr_of_days)
        am_pm_in_duration_hours = (duration_hours / 6)
        current_am_pm = start_time_split[1]
        am_pm = ''
        if current_am_pm == "PM" and am_pm_in_duration_hours / 12 == 0:
            am_pm += " PM"
        else:
            am_pm += " AM"
        hours = duration_hours % nr_of_days
        minutes = 0
        calculate_remain_muns = int(duration_minutes) + int(start_time_minutes)

        if calculate_remain_muns > 60:
            minutes = calculate_remain_muns - 60
        else:
            minutes = calculate_remain_muns

        minutes_str = "0"+ str(minutes)
        if hours == 0:
            new_time += "12:" + minutes_str[-2:] + am_pm + " (" + str(nr_of_days) + " days later)"
        else:
            new_time += str(hours) + ":" + minutes_str[-2:] + am_pm + " (" + str(nr_of_days) + " days later)"


    elif start_time_split[1] == "PM" and time_till_am_pm_swap < total_duration_minutes:
        new_time_hours = int((total_duration_minutes - time_till_am_pm_swap) / 60)
        print("new_time_hours", new_time_hours)
        new_time_minutes = (total_duration_minutes - time_till_am_pm_swap) - new_time_hours * 60
        new_time += str(int(new_time_hours)) + ":" + str(new_time_minutes) + " AM (next day)"

    elif start_time_split[1] == "AM" and (total_duration_minutes - time_till_am_pm_swap) < 60:
        new_time_minutes = int(total_duration_minutes - time_till_am_pm_swap)
        if len(str(new_time_minutes)) != 2:
            new_time += "12" + ":0" + str(new_time_minutes) + " PM"
        else:
            new_time += "12" + ":" + str(new_time_minutes) + " PM"

    elif start_time_split[1] == "AM" and time_till_am_pm_swap < total_duration_minutes:

        new_time_hours = int((total_duration_minutes - time_till_am_pm_swap) / 60)
        print("AM HOURS", new_time_hours)
        new_time_minutes = (total_duration_minutes - time_till_am_pm_swap) - new_time_hours * 60

        if len(str(new_time_minutes)) != 2:
            print("AM MINUTES", new_time_minutes)
            new_time += str(int(new_time_hours)) + ":0" + str(new_time_minutes) + " PM"
        else:
            new_time += str(int(new_time_hours)) + ":" + str(new_time_minutes) + " PM"

    elif start_time_split[1] == "PM" and time_till_am_pm_swap > total_duration_minutes:
        total_minutes = int((total_duration_minutes + start_time_to_minutes))
        new_time_hours = int(total_minutes / 60)
        print(new_time_hours)
        new_time_minutes = int(start_time_split[0].split(":")[1]) + int(duration_minutes)
        print(new_time_minutes)
        new_time += str(new_time_hours) + ":" + str(new_time_minutes) + " PM"

    if starting_day:
        return new_time + ", " + starting_day
    else:
        return new_time
