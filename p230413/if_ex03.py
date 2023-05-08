'''
# 조건문
# 조건 1개
if 조건:
    명령어
    명령어
# 조건 2개
if 조건:
    명령어
    명령어
else:
    명령어
    명령어
# 조건 3개 이상
if 조건:
    명령어
    명령어
elif 조건:
    명령어
    명령어
else:
    명령어
    명령어
'''
# 조건이 3개인 if문 
num = 0

if num > 0:
    print('양수')
elif num < 0:
    print('음수')
else:
    print('0')

print('== 프로그램 종료 ==')