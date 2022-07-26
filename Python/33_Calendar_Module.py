import calendar

mm, dd, year = map(int, input().split())
index = calendar.weekday(year, mm, dd)
print(list(calendar.day_name)[index].upper())
