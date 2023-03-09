import locale
from datetime import datetime, timedelta

locale.setlocale(locale.LC_TIME, 'ru_RU')

# Дата сегодня 
dt_now = datetime.now()
print(dt_now.strftime('Сегодня: %A %d %B %Y').capitalize())

# Дата вчера
delta_yeatarday = timedelta(days = 1)
td_yestarday = dt_now - delta_yeatarday
print(td_yestarday.strftime('Вчера: %A %d %B %Y').capitalize())

# Дата 30 дней назад
delta_30_days_before = timedelta(days = 30)
td_30_days_before = dt_now - delta_30_days_before
print(td_30_days_before.strftime('30 дней назад: %A %d %B %Y').capitalize())

# Преобразование даты из строки в формат datetime
dt_string = '01/01/25 12:10:03.234567'
date_dt = datetime.strptime(dt_string, '%m/%d/%y %H:%M:%S.%f')
print(date_dt)
