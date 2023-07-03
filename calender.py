import calendar

# Create a calendar for the whole year
year = 2023

# Iterate over the months and generate the calendar for each month
for month in range(1, 13):
    calendar_text = calendar.month(year, month)
    print(f"{'-'*20} {calendar.month_name[month]} {'-'*20}")
    print(calendar_text)
    print()
    
#this code is for calender of year 2023