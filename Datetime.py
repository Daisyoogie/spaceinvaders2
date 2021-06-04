import datetime

import pytz

today = datetime.date.today()
print(today)
birthday = datetime.date(1969,1,18)
print(birthday)

# finds days since birth
days_since_birth = (today - birthday)
print(days_since_birth)
# adds 10 days to current day
tdelta = datetime.timedelta(days=10)
print(today + tdelta)
tdelta = datetime.timedelta(days=10)
print(today - tdelta)

print(today.month)
print(today.day)
print(today.weekday())
#monday is = 0
print(datetime.time(7, 2, 20, 15))

# datetime.date (Y, M, D)
# datetime.time (h, m, s, ms)
# datetime.datetime (Y, M, D, h, m, s, ms)
hour_delta = datetime.timedelta(hours=10)
print(datetime.datetime.now())
# adds 10 hours to current day
hour_delta = datetime.timedelta(hours=10)
print(datetime.datetime.now() + hour_delta)

datetime_today = datetime.datetime.now(tz=pytz.UTC)
datetime_pacific = datetime_today.astimezone(pytz.timezone('US/pacific'))
print(datetime_pacific)
for tz in pytz.all_timezones:
    print(tz)








