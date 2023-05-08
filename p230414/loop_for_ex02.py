# 리스트 내포
# [문법] [명령어 for 변수 in 여러값]
# [문법] [명령어 for 변수 in 여러값 if 조건식]

for r in range(1, 10):
    print(r, end=' ')

# 리스트 내포 1)
print('\n==리스트 내포==')
[print(r, end=' ') for r in range(1, 10)]

# 리스트 내포 2)
even = [r for r in range(2, 11, 2)]
print('\neven >>', even)
print('even type >>', type(even))

# 위 코드를 일반 for문으로 변경
even = []
for r in range(2, 11, 2):
    even.append(r)
print('even >>', even)
print('even type >>', type(even))