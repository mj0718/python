# [방법 2] from 모듈명 import 클래스명,함수,변수명
from datetime import datetime as dt
from datetime import date

# 날짜와 시간
now = dt.now()
print('now >>', now)

# 날짜 1 : datetime
date = dt.now().date()
print('date >>', date)

# 년
year = dt.now().year
print('year >>', year)

# 월
month = now.month
print('month >>', month)

# 일
day = now.day
print('day >>', day)

# 시간
time = dt.now().time()
print('time >>', time)

print('hour >>', time.hour)
print('minute >>', time.minute)
print('second >>', time.second)

# 날짜 2 : date
today = date.today()
print('today >>', today)
print('year >>', today.year)
print('month >>', today.month)
print('day >>', today.day)

# # [방법 3] import 모듈명 as 별칭
# import datetime as dt

# # 날짜와 시간
# now = dt.datetime.now()
# print('now >>', now)

# # 날짜 1 : datetime
# date = now.date()
# print('date >>', date)

# # 년
# year = now.year
# print('year >>', year)

# # 월
# month = now.month
# print('month >>', month)

# # 일
# day = now.day
# print('day >>', day)

# # 시간
# time = dt.datetime.now().time()
# print('time >>', time)

# print('hour >>', time.hour)
# print('minute >>', time.minute)
# print('second >>', time.second)

# # 날짜 2 : date
# today = dt.date.today()
# print('today >>', today)
# print('year >>', today.year)
# print('month >>', today.month)
# print('day >>', today.day)
