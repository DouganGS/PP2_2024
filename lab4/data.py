from datetime import datetime
from datetime import timedelta

#1

time_now = datetime.now()
subtracted_days = (time_now.day) - 5

result_data = datetime(time_now.year,time_now.month, subtracted_days, time_now.hour,time_now.minute, time_now.second)
print('Subtracted date:',result_data,'\n')

#2

today = datetime.now()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print('Yesterday date:', yesterday.strftime('%Y-%m-%d %H:%M:%S'), '\nToday date:', today.strftime('%Y-%m-%d %H:%M:%S'), '\nTomorrow date',tomorrow.strftime('%Y-%m-%d %H:%M:%S'),'\n')

#3

today_date = datetime.now()

print(today_date.strftime('%Y-%m-%d %H:%M:%S'))

#4

date = "2024-02-24"
new_date = "2024-02-19"
date1 = datetime.datetime.strptime(date, '%Y-%m-%d')
date2 =datetime.datetime.strptime(new_date, '%Y-%m-%d')

difference_in_seconds = (date1-date2)/1000

print(difference_in_seconds)

