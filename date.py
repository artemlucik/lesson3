from datetime import date, timedelta, datetime
today_date = date.today()
yesterday = today_date - timedelta(days = 1)

last_day_in_prev_month = date.today().replace(day = 1) - timedelta(days = 1)
last_day = last_day_in_prev_month.strftime('%d')
prev_month_daye = today_date - timedelta(days = int(last_day))

print(f'Today is: {today_date}')
print(f'Yesterday was: {yesterday}')
print(f'Last month: {prev_month_daye}')

#--------------------------------------#
date_string = '01/01/17 12:10:03.234567'
date_dt = datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f')
print(date_dt)
