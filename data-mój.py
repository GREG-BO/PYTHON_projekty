import arrow

time_str = time.strftime("%d %m %Y\n%H:%M:%S")
print(time_str)

print(time_str)


tz_NY = pytz.timezone('America/New_York')
datetime_NY = datetime.now(tz_NY)
print("NY time:", datetime_NY.strftime("%H:%M:%S"))

tz_London = pytz.timezone('Europe/London')
datetime_London = datetime.now(tz_London)
print("London time:", datetime_London.strftime("%H:%M:%S"))

tz_Warsaw = pytz.timezone('Europe/Warsaw')
datetime_Waw = datetime.now(tz_Warsaw)
print("Warsaw time:", datetime_Waw.strftime("%H:%M:%S")
