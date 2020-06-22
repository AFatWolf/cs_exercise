import datetime
import calendar
now = datetime.datetime.now()
print(now)
print(now.year)
print(now.month)
print(now.weekday())
print(now.day)
print(now.isocalendar()[1])
print(calendar.day_name[now.weekday()])
print(now.timetuple().tm_yday)

