'''
[모듈 읽어오기]
1) import 모듈명
2) from 모듈명 import 클래스명,함수명,변수명
3) import 모듈명 as 별칭
'''
# [방법 1]
import random
print('random value >>', random.random())
print('random.uniform(min, max) >>', random.uniform(1, 10)) # min~max 사이의 랜덤값 실수로 출력
print('random.randrange(min, max) >>', random.randrange(1, 10)) # min~max 사이의 랜덤값 정수로 출력(1~9까지 값)
print('random.randrange(min, max) >>', random.randrange(10)) # 0~max 사이의 랜덤값 정수로 출력(0~9까지 값)
print('random.choice(여러값) >>', random.choice([2, 4, 6, 8])) #여러 값 중 랜덤으로 하나를 선택

# [방법 2]
# from random import random
# print('random value >>', random())

# [방법 3]
# import random as rd
# print('random value >>', rd.random())