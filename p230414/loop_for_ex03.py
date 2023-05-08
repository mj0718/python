# 리스트 내포
# [문법] [명령어 for 변수 in 여러값]
# [문법] [명령어 for 변수 in 여러값 if 조건식]

# 일반 for문
for r in range(1, 11):
    if r % 3 == 0:
        print(r, end=' ')
print()

# 리스트 내포 1)
[print(r, end=' ') for r in range(1, 11) if r % 3 == 0]
print()

# 일반 for문
even = list() # 빈 리스트
for r in range(1, 10):
    if r % 2 == 0:
        even.append(r)
print('even >>', even)

# 리스트 내포 2)
even_two = [r for r in range(1, 10) if r % 2 == 0]
print('even_two >>', even_two)