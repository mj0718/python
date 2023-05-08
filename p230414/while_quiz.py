idx = 1
data = []

while idx <= 5:
    user_value = int(input(f'[{idx}번째] 1 이상의 정수를 입력 ... '))
    data.append(user_value)
    # print('data >>', data)
    idx = idx + 1

print('누적 합 >>', sum(data))
print('입력된 값 모두 출력 :', data)