def add_time(start, duration, day=None):
  ''' This function accepts a start time, duration and optionally day of week,
      and reports new time
      Sample call 1  : add_time("11:59 PM", "24:05", "Wednesday")
      Sample output 1: 12:04 AM, Friday (2 days later)
      Sample call 2  : add_time("9:15 PM", "5:30")
      Sample output 2: 2:45 AM (next day)'''
  # defining days of week

  dow = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
  dow_lower = [x.lower() for x in dow]

  # Filling the lists

  start = start.split(" ")
  time = start[0].split(":")
  time = [int(x) for x in time]
  selector = start[1]
  duration = duration.split(":")
  duration = [int(x) for x in duration]

  if duration[1] > 60:
    out = "Error: Minutes cannot be more than 60."

  # Converting military time format

  if selector == "PM":
    time[0] = time[0] + 12

  # Calculating new time

  hour = (time[0] + duration[0]) % 24 + (time[1] + duration[1]) // 60
  min = (time[1] + duration[1]) % 60
  days = ((time[0] + duration[0]) + (time[1] + duration[1]) // 60) // 24
  if day is None:
    pass
  else:
    day = day.lower()
    day_no = dow_lower.index(day)
    new_day_no = (days + day_no) % 7
    new_day = dow[new_day_no]

  if hour >= 12 and hour < 24:
    selector = "PM"
    hour = hour if hour == 12 else hour - 12
  elif hour == 24:
    selector = "AM"
    hour = 12
  else:
    selector = "AM"

  if days == 0:
    if day is None:
      out = f"{hour}:{min if min >= 10 else '0' + str(min)} {selector}"
    else:
      out = f"{hour}:{min if min >= 10 else '0' + str(min)} {selector}, {new_day}"
  elif days == 1:
    if day is None:
      out = f"{hour}:{min if min >= 10 else '0' + str(min)} {selector} (next day)"
    else:
      out = f"{hour}:{min if min >= 10 else '0' + str(min)} {selector}, {new_day} (next day)"
  else:
    if day is None:
      out = f"{hour}:{min if min >= 10 else '0' + str(min)} {selector} ({days} days later)"
    else:
      out = f"{hour}:{min if min >= 10 else '0' + str(min)} {selector}, {new_day} ({days} days later)"

  return out

if __name__ == '__main__':
  print(add_time("3:30 PM", "2:12"))
  print(add_time("11:55 AM", "3:12"))
  print(add_time("9:15 PM", "5:30"))
  print(add_time("11:40 AM", "0:25"))
  print(add_time("2:59 AM", "24:00"))
  print(add_time("11:59 PM", "24:05"))
  print(add_time("8:16 PM", "466:02"))
  print(add_time("5:01 AM", "0:00"))
  print(add_time("3:30 PM", "2:12", "Monday"))
  print(add_time("2:59 AM", "24:00", "saturDay"))
  print(add_time("11:59 PM", "24:05", "Wednesday"))
  print(add_time("8:16 PM", "466:02", "tuesday"))

