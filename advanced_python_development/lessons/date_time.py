from datetime import datetime, timedelta, timezone

# Gives current time for where the program is running. AKA in California time
current_time = datetime.now()

# Timezone by utc. programs should ALWAYS be utc
# data should stored as utc
# Only time it should not be utc, is when DISPLAYING time to a user
current_timezone_time = datetime.now(timezone.utc)

# Get tomorrow's time
today = datetime.now(timezone.utc)
tomorrow = today + timedelta(days=1)

# format date time objects in month-day-year format
# %m = month %d = day %Y = year %H = hour %M = minute %S = second
clean_date = today.strftime('%m-%d-%Y')
clean_time = today.strftime('%H:%M')
print(clean_date)
print(clean_time)

# Collect date
user_date = input('Enter date in mm-dd-yyyy: ')
# Create a datetime object from data
time_format = datetime.strptime(user_date, '%m-%d-%Y') 