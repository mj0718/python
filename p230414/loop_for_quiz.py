# [문제 1] 2단을 출력
# 출력형태 
# 2 * 1 = 2
# 2 * 2 = 4
# ...
# 2 * 9 = 18

# for r in range(1, 10):
#     print(f'2 * {r} = {r * 2}')

[print(f'2 * {r} = {r * 2}') for r in range(1, 10)]
print()

# [문제 2] 60점 이상인 학생의 번호와 점수 출력
# 출력형태
# 1번 학생은 90점으로 합격입니다. 
math = [90, 45, 60, 75, 50]
# for m in math:
#     if m >= 60:
#         print(f'{math.index(m)+1}번 학생은 {m}점으로 합격입니다.')

# [print(f'{math.index(m)+1}번 학생은 {m}점으로 합격입니다.') for m in math if m >= 60]
# print()

## [방법 1] =====================================
# idx = 1

# for m in math:
#     if m >= 60:
#         print(f'{idx}번 학생은 {m}점으로 합격')
    
#     idx += 1

## [방법 2-1] ===================================
# for idx, m in enumerate(math, 1):
#     if m >= 60:
#         print(f'{idx}번 학생은 {m}점으로 합격')

## [방법 2-2] ===================================
for m in enumerate(math, 1):
    if m[1] >= 60:
        print(f'{m[0]}번 학생은 {m[1]}점으로 합격')

# [문제 3] 60점 이상인 학생의 이름과 점수 출력
# 출력형태
# 홍길동 학생은 90점으로 합격입니다. 
math = {'홍길동': 90, '박보검': 45, '이미자': 60, '이길동': 75, '하하': 50}
## [방법 1] ==========================================
# for key in math:
#     if math[key] >= 60:
#         print(f'{key} 학생은 {math[key]}점으로 합격')

## [방법 2] ==========================================
# for key, value in math.items():
#     if value >= 60:
#         print(f'{key} 학생은 {value}점으로 합격입니다.')

## [방법 3] ==========================================
# for m in math.items():
#     if m[1] >= 60:
#         print(f'{m[0]} 학생은 {m[1]}점으로 합격입니다.')

# [print(f'{key} 학생은 {value}점으로 합격입니다.') for key, value in math.items() if value >= 60]

[print(f'{m[0]} 학생은 {m[1]}점으로 합격입니다.') for m in math.items() if m[1] >= 60]