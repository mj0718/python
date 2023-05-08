""" 
조건 연산자
True일때 if 조건 else False일때 
 """

n1, n2 = 5, 3
print('n1 크다' if n1 > n2 else 'n1 작다')

# 문제
# n1과 n2를 비교하여 큰 값을 result에 저장하여 출력

result = n1 if n1 > n2 else n2
print('result >>', result)