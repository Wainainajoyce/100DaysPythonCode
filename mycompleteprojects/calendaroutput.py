import calendar

print(calendar.month(2023, 8))
#An error occured due to naming the file "calendar" that is same as the method.

# Get the calendar for a specific year and month
cal = calendar.month(2023, 8)
print("Calendar for August 2023:")
print(cal)

# Check if a year is a leap year
is_leap = calendar.isleap(2024)
print("Is 2024 a leap year?", is_leap)

# Get the first weekday of a month
first_weekday = calendar.weekday(2023, 8, 1)
print("First weekday of August 2023:", first_weekday)

# Get the day of the week for a specific date
day_of_week = calendar.weekday(2023, 8, 15)
print("Day of the week for August 15, 2023:", day_of_week)

# Get the day of the week as a string
day_name = calendar.day_name[day_of_week]
print("Day of the week:", day_name)

# Print the calendar for an entire year
year_calendar = calendar.TextCalendar().formatyear(2023)
print("Calendar for the year 2023:")
print(year_calendar)
