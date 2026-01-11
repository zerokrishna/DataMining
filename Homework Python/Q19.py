import datetime

d = datetime.date.today()
t = datetime.datetime.now()
print(f'Today date : {d.year}/{d.month}/{d.day}')
print(f'Time now : {t.hour}:{t.minute}:{t.second}')