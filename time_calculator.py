def add_time(start_time, duration, start_day=""):
    time, am_pm = start_time.split(" ")
    start_hours, start_mins = [int(time_component) for time_component in time.split(":")]
    duration_hours, duration_mins = [int(time_component) for time_component in duration.split(":")]
    end_hours = start_hours + duration_hours
    end_minutes = start_mins + duration_mins
    end_am_pm = am_pm
    end_days_later = 0

    if end_minutes >= 60:
        end_hours += 1
        end_minutes = end_minutes - 60
    print(f"    Initial end values: {end_hours}:{end_minutes} {end_am_pm} ({end_days_later} days later)")

    while end_hours > 12:
        end_am_pm = "PM" if end_am_pm == "AM" else "AM"
        if end_am_pm == "AM":
            end_days_later += 1
        end_hours -= 12
        print(f"   Updates end values: {end_hours}:{end_minutes} {end_am_pm} ({end_days_later} days later)")

    if start_hours < 12 and end_hours == 12:  # special case
        end_am_pm = "PM" if end_am_pm == "AM" else "AM"
        if end_am_pm == "AM":
            end_days_later += 1
        print(f"    Updates end values: {end_hours}:{end_minutes} {end_am_pm} ({end_days_later} days later)")

    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    end_time = f"{end_hours}:{end_minutes:02} {end_am_pm}" + end_days_later_text(end_days_later, start_day, weekdays)

    print(f"Final end values: {end_time}")
    return end_time


def end_days_later_text(end_days_later, start_day, weekdays):
    start_day_normalize = start_day.lower().title()
    start_index = weekdays.index(start_day_normalize) # 6

    if end_days_later == 0 and start_day != "":
        return ", " + start_day_normalize
    if end_days_later == 0 and start_day == "":
        return ""
    if end_days_later == 1 and start_day != "":
        updated_day = ""
        update_week = weekdays[start_index:] + weekdays[:start_index]
        updated_day += update_week[update_week.index(start_day_normalize) + 1]
        return ", " + updated_day + " (next day)"
    if end_days_later == 1 and start_day == "":
        return " (next day)"

    return f" ({end_days_later} days later)"


# def end_days_later_text(end_days_later):
#     if end_days_later == 0:
#         return ""
#     if end_days_later == 1:
#         return " (next day)"
#     return f" ({end_days_later} days later)"

#
# if __name__ == "__main__":
#     add_time("5:40 AM", "1:10")   # 6:50 AM
#     add_time("5:55 PM", "0:10")   # 6:05 PM ZERO MISSING
#     add_time("11:11 AM", "1:00")  # 12:11 PM
#     add_time("11:11 AM", "10:00")  # 9:11 PM
#     add_time("6:30 PM", "205:12")  # 7:42 AM (9 days later)
#     add_time("11:55 PM", "0:06")  # 12:01 AM (1 days later)
#
