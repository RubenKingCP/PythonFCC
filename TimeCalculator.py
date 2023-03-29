def add_time(curtime, spendtime, passday = None):
    days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    day = str(passday).lower()
    position = None
    counter = 0
    if passday is not None:
        position = int(days.index(day))
    expanded = curtime.split(" ")
    time = expanded[0].split(":")
    hours = int(time[0])
    minutes = int(time[1])
    am_pm = expanded[1]
    toggle = None
    if am_pm == "AM":
        toggle = True
    elif am_pm == "PM":
        toggle = False
    spendtime_expanded = spendtime.split(":")
    hours_to_add = int(spendtime_expanded[0])
    minutes_to_add = int(spendtime_expanded[1])
    hours_total = hours + hours_to_add
    minutes_total = minutes + minutes_to_add
    if minutes_total > 59:
        hours_total += 1
        minutes_total -= 60
    while hours_total > 12:
        if hours_total > 12:
            hours_total -= 12
        if toggle is True:
            toggle = False
        elif toggle is False:
            toggle = True
            if position is not None:
                position += 1
            counter += 1
    if hours_total == 12 and minutes_total > 0:
          if toggle is True:
            toggle = False
          elif toggle is False:
            toggle = True
            if position is not None:
              position += 1
            counter += 1
    if toggle is True:
        am_pm = "AM"
    elif toggle is False:
        am_pm = "PM"
    if minutes_total < 10:
            minutes_total = "0" + str(minutes_total)
    time_string = str(hours_total) + ":" + str(minutes_total) + " " + am_pm
    if position is not None:
        test1 = position % 7
        time_string += ", " + days[test1].capitalize()
    if counter != 0:
      if counter == 1:
        time_string += " (next day)"
      else:
        time_string += " " + "(" + str(counter) + " days later)"
    return time_string
