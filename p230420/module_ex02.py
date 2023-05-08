# [방법 1] import 모듈명
import datetime

# 날짜와 시간
now = datetime.datetime.now()
print('now >>', now)

# 날짜 1 : datetime
date = datetime.datetime.now().date()
print('date >>', date)

# 년
year = datetime.datetime.now().year
print('year >>', year)

# 월
month = now.month
print('month >>', month)

# 일
day = now.day
print('day >>', day)

# 시간
time = datetime.datetime.now().time()
print('time >>', time)

print('hour >>', time.hour)
print('minute >>', time.minute)
print('second >>', time.second)

# 날짜 2 : date
today = datetime.date.today()
print('today >>', today)
print('year >>', today.year)
print('month >>', today.month)
print('day >>', today.day)