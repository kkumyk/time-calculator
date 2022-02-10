def add_time(start, duration, starting_day=False):
    half_day_minutes = 12 * 60
    one_day_minutes = 24 * 60

    start_time_split = start.split()
    start_h = int(start_time_split[0].split(":")[0])
    start_h_to_m = int(start_time_split[0].split(":")[0]) * 60
    start_m = int(start_time_split[0].split(":")[1])
    total_start_m = start_h_to_m + start_m
    start_am_or_pm = start_time_split[1]
    # m_before_am_pm_swap = half_day_minutes - total_start_m

    duration_split = duration.split()
    duration_h = int(duration_split[0].split(":")[0])
    duration_h_to_m = duration_h * 60
    duration_m = int(duration_split[0].split(":")[1])
    total_duration_m = duration_h_to_m + duration_m

    end_minutes = start_m + duration_m
    if end_minutes >= 60:
        start_h += 1
        end_minutes = end_minutes % 60
        end_minutes_zero = "0" + str(end_minutes)

    nr_hours = (start_h + duration_h) % 12
    end_hours = ''
    if nr_hours == 0:
        end_hours += str(12)
    else:
        end_hours += str(nr_hours)

    print("END HOURS", end_hours, end_minutes)

    new_time = end_hours + ":" + end_minutes_zero[-2:] + " "

    return new_time

    # nr_of_days = 0
    # # find out if duration hours contain days
    # raw_days_count = duration_h_to_m / one_day_minutes
    # if raw_days_count > round(raw_days_count):
    #     nr_of_days += round(raw_days_count) + 1
    # else:
    #     nr_of_days += round(raw_days_count)
    #
    # am_pm = ''
    # # hours_minus_days = duration_h_to_m - round(raw_days_count)*one_day_minutes
    # # print("days_minus_hours", duration_h_to_m, hours_minus_days)
    #
    #
    #
    #
    # new_time = ''
    #
    # if duration == "0:00":  # test_no_change: return start time if h and m == 0
    #     new_time += start
    #
    # elif duration == "24:00":  # test_twenty_four: return same time, next day
    #     new_time += start + " (next day)"
    #
    #
    #
    #
    # elif total_duration_m > one_day_minutes:  # count nr of days later than one day
    #
    #     # days in the future minus total mins to add and minus minutes bef
    #     remaining_m = nr_of_days * one_day_minutes - (total_duration_m + (60-start_m))
    #
    #     print("left", remaining_m)
    #     print("nr_of_days", nr_of_days)
    #
    #     if start_am_or_pm == "PM" and remaining_m > half_day_minutes:
    #         am_pm += " AM"
    #     else:
    #         am_pm += " PM"
    #
    #
    #
    #
    #
    #     hours = duration_h % nr_of_days
    #     minutes = 0
    #     calculate_remain_muns = int(duration_m) + int(start_m)
    #
    #     if calculate_remain_muns > 60:
    #         minutes = calculate_remain_muns - 60
    #     else:
    #         minutes = calculate_remain_muns
    #
    #     minutes_str = "0" + str(minutes)
    #     if hours == 0:
    #         new_time += "12:" + minutes_str[-2:] + am_pm + " (" + str(nr_of_days) + " days later)"
    #     else:
    #         new_time += str(hours) + ":" + minutes_str[-2:] + am_pm + " (" + str(nr_of_days) + " days later)"
    #
    # elif start_am_or_pm == "PM" and m_before_am_pm_swap < total_duration_m:
    #     new_time_hours = int((total_duration_m - m_before_am_pm_swap) / 60)
    #     #print("new_time_hours", new_time_hours)
    #
    #     new_time_minutes = (total_duration_m - m_before_am_pm_swap) - new_time_hours * 60
    #     minutes_str = "0" + str(new_time_minutes)
    #     #print("New_time_minutes", minutes_str)
    #
    #     new_time += str(int(new_time_hours)) + ":" + minutes_str[-2:] + " AM (next day)"
    #
    # elif start_am_or_pm == "AM" and (total_duration_m - m_before_am_pm_swap) < 60:
    #     new_time_minutes = int(total_duration_m - m_before_am_pm_swap)
    #     if len(str(new_time_minutes)) != 2:
    #         new_time += "12" + ":0" + str(new_time_minutes) + " PM"
    #     else:
    #         new_time += "12" + ":" + str(new_time_minutes) + " PM"
    #
    # elif start_am_or_pm == "AM" and m_before_am_pm_swap < total_duration_m:
    #
    #     new_time_hours = int((total_duration_m - m_before_am_pm_swap) / 60)
    #     #print("AM HOURS", new_time_hours)
    #     new_time_minutes = (total_duration_m - m_before_am_pm_swap) - new_time_hours * 60
    #
    #     if len(str(new_time_minutes)) != 2:
    #         #print("AM MINUTES", new_time_minutes)
    #         new_time += str(int(new_time_hours)) + ":0" + str(new_time_minutes) + " PM"
    #     else:
    #         new_time += str(int(new_time_hours)) + ":" + str(new_time_minutes) + " PM"
    #
    # elif start_am_or_pm == "PM" and m_before_am_pm_swap > total_duration_m:
    #     total_minutes = int((total_duration_m + total_start_m))
    #     new_time_hours = int(total_minutes / 60)
    #     #print(new_time_hours)
    #     new_time_minutes = int(start_time_split[0].split(":")[1]) + int(duration_m)
    #     #print(new_time_minutes)
    #     new_time += str(new_time_hours) + ":" + str(new_time_minutes) + " PM"
    #
    #
    #
    #
    #
    #
    #
    # weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "Monday", "Tuesday",
    #             "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    #
    # if starting_day and "(next day)" in new_time:
    #     starting_day_norm = starting_day.lower().capitalize()
    #     post_day = weekdays[weekdays.index(starting_day_norm) + 1]
    #     updated_new_time = new_time.split("(")[0].rstrip() + ", " + post_day + " (" + new_time.split("(")[1]
    #     return updated_new_time
    #
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
