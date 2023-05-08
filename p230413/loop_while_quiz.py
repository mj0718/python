# [문제 1] while문을 이용하여 1부터 100까지 출력하시오.
# 단, 가로로 출력 
# 출력 형태 : 1 2 3 .... 100
num = 1
while num <= 100:
    print(num, end=' ')
    num += 1

# [문제 2] 2단을 출력하시오.
# 출력형태 
# 2 * 1 = 2
# 2 * 2 = 4
# ...
# 2 * 9 = 18
print('\n==2단 출력==')
num = 1
while num < 10:
    # print('2 * %d = %d'%(num, num*2))
    print(f'2 * {num} = {2 * num}')
    num += 1

# [문제 3] 1~10 누적합
# 출력형태 : 1~10 누적합 >> 55
# [방법 1]
# num = 1
# total = 0
# while num < 11:
#     total += num
#     num += 1
# print('1~10 누적합 >>', total)

# [방법 2]
print('1~10 누적합 >>', sum(range(1,11)))

# [문제 4] 리스트 변수 number의 모든 요소의 합을 출력하시오.
# [방법 1]
number = [2, 5, 9, 7, 11]
# total, idx = 0, 0
# while idx < len(number):
#     total += number[idx]
#     idx += 1
# print('모든 요소의 합 >>', total)

# [방법 2]
print('전체 합 >>', sum(number))