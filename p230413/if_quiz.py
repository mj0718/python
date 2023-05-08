value = 7

# [문제 1] value에 저장된 값이 짝수/홀수 출력
if value % 2 == 0:
    print('짝수입니다')
else:
    print('홀수입니다.')

# [문제 2] value에 저장된 값의 범위 출력
# 범위: 0미만의 수, 0이상 10미만의 수, 10이상 20미만의 수, 
# 20이상 30미만의 수, 30이상의 수
if value < 0: 
    print('0미만의 수')
elif value < 10:
    print('0이상 10미만의 수')
elif value < 20:
    print('10이상 20미만의 수')
elif value < 30:
    print('20이상 30미만의 수')
else:
    print('30이상의 수')

# [문제 3] n1과 n2를 비교하여, 큰 값을 출력
n1, n2 = 5, 3

# [방법 1]
# if n1 > n2:
#     print('큰 값 >>', n1)
# else:
#     print('큰 값 >>', n2)

# [방법 2]
# if n1 > n2:
#     print('큰 값 >>', n1)
# elif n1 < n2:
#     print('큰 값 >>', n2)

# [방법 3]
print('큰 값 >>', max(n1, n2))

# [문제 4] 복숭아가 있으면 복숭아 개수를 출력하고, 없으면 '복숭아 없습니다' 출력
# 복숭아 개수는 7개입니다.
# 복숭아 없습니다.
fruit = {'사과': 5, '복숭아': 7, '바나나': 3}

if '복숭아' in fruit:
    # print('복숭아 개수는' + str(fruit['복숭아']) +'개입니다.')
    # print('복숭아 개수는 %d개입니다.'%fruit['복숭아'])
    # print('복숭아 개수는 {}개입니다.'.format(fruit['복숭아']))
    print(f'복숭아 개수는 {fruit["복숭아"]}개입니다.')
else:
    print('복숭아 없습니다.')

# cf) + 연산자는 서로 타입이 같아야함
# print(5 + 3)
# print('문자열1' + '문자열2')
# print('문자열1' + 5) Error
# print(str(5) + '문자열1') 