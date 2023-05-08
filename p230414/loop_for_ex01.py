'''
# 반복문 : for
for 변수 in 여러값:
    명령어
    명령어
'''
even = [2, 4, 6]

for en in even:
    print(en)

# range 함수
# [인수 1개] range(끝값) 0부터 시작
print('== range 함수 1) ==')
for r in range(10):
    print(r, end=' ')

# [인수 2개] range(시작값, 끝값) 끝값은 제외됨
print('\n== range 함수 2) ==')
for r in range(1, 10):
    print(r, end=' ')

# [인수 3개] range(시작값, 끝값, 증감값)
print('\n== range 함수 3) ==')
for r in range(1, 10, 2):
    print(r, end=' ')

# [문제] 다음과 같이 출력하시오. 
# 10 9 8 7 6 5 4 3 2 1
print('\n==문제==')
for r in range(10, 0, -1):
    print(r, end=' ')

# [문제] 다음과 같이 출력하시오. 
# 2 4 6 8 10
print('\n==문제==')
for r in range(2, 11, 2):
    print(r, end=' ')


# [문제] 리스트 변수 number의 모든 요소의 합을 출력하시오.
number = [2, 5, 9, 7, 11]
total = 0
for num in number:
    total += num
print('\n전체 합 >>', total)