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
# 조건이 2개인 if문 
num = 2

if num >= 5:
    num += 1
else:
    print('조건이 False일 때 실행되는 영역')
    print('=' * 30)

print('num >>', num)