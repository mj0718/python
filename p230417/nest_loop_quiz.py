## [문제 1] 2~9단 출력
for i in range(2, 10):
    for j in range(1, 10):
        print(f'{i} * {j} = {i*j}')
    print()

## [문제 2] 짝수단 출력
for i in range(2, 10, 2):
    for j in range(1, 10):
        print(f'{i} * {j} = {i*j}')
    print()

## [문제 3] 다음과 같이 출력
for i in range(2, 10, 2):
    for j in range(1, i+1):
         print(f'{i} * {j} = {i*j}')
    print()