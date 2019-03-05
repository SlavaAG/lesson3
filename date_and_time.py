from datetime import datetime, timedelta
import locale


delta_day = timedelta(days=1)
delta_month = timedelta(days=30)
today = datetime.now()
yesterday = today - delta_day
last_month = today - delta_month

date_string = '01/01/17 12:10:03.234567'
date_dt = datetime.strptime(date_string, '%m/%d/%y %H:%M:%S.%f')

locale.setlocale(locale.LC_ALL, 'russian')
print('Вчера ', yesterday.strftime('%A %d %B %Y'))
print('Сегодня ', today.strftime('%A %d %B %Y'))
print('Месяц назад ', last_month.strftime('%A %d %B %Y'))
print('Просто дата ', date_dt)