def add_time(start, duration, starting_day=False):
    total_am_pm_minutes = 12 * 60
    print("total_am_pm_minutes", total_am_pm_minutes)
    start_time_split = start.split()
    start_h_to_minutes = int(start_time_split[0].split(":")[0]) * 60
    start_time_to_minutes = start_h_to_minutes + int(start_time_split[0].split(":")[1])
    print("start_time_to_minutes", start_time_to_minutes)
    time_till_am_pm_swap = total_am_pm_minutes - start_time_to_minutes
    print("time_till_am_pm_swap", time_till_am_pm_swap)

    duration_split = duration.split()
    duration_hours = int(duration_split[0].split(":")[0])
    duration_h_to_minutes = duration_hours * 60
    duration_minutes = (duration_split[0].split(":")[1])
    print(duration_minutes)
    # print("duration hours, duration_h_to_minutes", duration_hours, duration_h_to_minutes)
    total_duration_minutes = int(duration_h_to_minutes) + int(duration_minutes)
    print("total_duration_minutes", total_duration_minutes)
    # minutes_sum = int(start_time_to_minutes) + int(duration_minutes)

    new_time = ''
    if start_time_split[1] == "PM" and time_till_am_pm_swap < total_duration_minutes:
        new_time_hours = int((total_duration_minutes - time_till_am_pm_swap) / 60)
        print("new_time_hours", new_time_hours)
        new_time_minutes = (total_duration_minutes - time_till_am_pm_swap) - new_time_hours * 60
        new_time += str(int(new_time_hours)) + ":" + str(new_time_minutes) + " AM (next day)"

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


    # else:
    #     new_time_hours = int((total_duration_minutes - time_till_am_pm_swap) / 60)
    #     print("AM HOURS", new_time_hours)
    #     new_time_minutes = (total_duration_minutes - time_till_am_pm_swap) - new_time_hours * 60
    #     new_time += str(int(new_time_hours)) + ":" + str(new_time_minutes) + " PM"


    return new_time



    # # else:
    #     new_time_hours = int(start_time_split[0].split(":")[0]) + int(duration_split[0].split(":")[0])
    #     print("new_time_hours", new_time_hours)
    #     minutes = int(start_time_split[0].split(":")[1]) + int(duration_split[0].split(":")[1])
    #     if len(str(minutes)) == 2:
    #         new_time_minutes = minutes
    #     else:
    #         new_time_minutes = "0" + str(minutes)




    # hours_sum = int(start_hour) + int(duration_hour)
    # minutes_sum = int(start_minutes) + int(duration_minutes)
    # print("HOURS", hours_sum)
    # print("MINUTES", minutes_sum)

    # new_time = ''
    # new_time_check = ''
    # new_time_check += str(hours_sum) + ":" + str(minutes_sum)
    # # print("new_time_check::", new_time_check)
    # if start_am_pm == "PM" and int(hours_sum) < 13:
    #     new_time += new_time_check + " PM"
    # else:
    #     trans_time = new_time_check.split(':')
    #     trans_hours = int(trans_time[0])*60
    #     trans_minutes = trans_hours + int(trans_time[1])
    #     trans_start_time_to_minutes = int(start_hour)*60 + int(start_minutes)
    #     # print("trans_minutes", trans_minutes)
    #     # print(" trans_start_time_to_minutes",  trans_start_time_to_minutes)
    #     min_dif = trans_minutes - trans_start_time_to_minutes
    #     new_hours = round(min_dif/60)
    #     # print("new_hours", new_hours)
    #     new_minutes = (min_dif - 3*60) - (60 - int(start_minutes))
    #     if len(str(new_minutes)) == 2:
    #         new_time += str(new_hours) + ":" + str(new_minutes) + " PM"
    #
    #
    #
    #
    #     else:
    #         new_time += str(new_hours) + ":" + "0" + str(new_minutes) + " PM"
