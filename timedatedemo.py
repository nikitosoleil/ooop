from time import time
from datetime import datetime
from timedate import TimeDate

timestamp = time()  # choose whatever integer representing unix time here
print('timestamp: ', timestamp)
# NOTE: some timestamps may cause an error with built-in datetime.fromtimestamp() function, not with mine though
td = TimeDate.from_timestamp(timestamp)  # converting forth
print('td: ', td)  # showing how timestamp was converted to date and time
td = TimeDate.from_date_and_time(td.year, td.month + 1, td.day_of_month + 1, td.hours, td.minutes, td.seconds)  # converting back
print('td: ', td)  # showing how date and time were converted to day of week
print('int(td): ', int(td))  # showing how date and time were converted to unix time

date_and_time_string = '2018-09-30 20:35:00'  # choose whatever date and time in YYYY-MM-DD HH:MM:SS format here
td = TimeDate(date_and_time_string)  # converting
print('td: ', td)  # showing how constructor from string done its job

print('datetime.fromtimestamp(timestamp): ', datetime.fromtimestamp(timestamp))  # sanity check with built-in stuff here

td2 = TimeDate.from_timestamp(timestamp + 86461)  # again, feel free to choose whatever parameter value here
print('td2: ', td2)
delta = td2-td  # find difference between two points in time whatever that means
# actually, difference is expressed in terms of years, months, etc. and in terms of absolute second simultaneously
print('delta: ', delta)  # representation in terms of years, months, days, hours, minutes and seconds, by default
print('int(delta): ', int(delta))  # in terms of absolute seconds
td0 = TimeDate.from_timestamp(-1)  # another random point in time
print('td0: ', td0)
td_sum = td0 + delta  # when we add something to a point in time, it makes sense to add absolute seconds, not years which can differ
print('td_sum: ', td_sum)
