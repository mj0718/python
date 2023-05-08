prompt = '''
--------------
1. 추가
2. 삭제
3. 목록
4. 종료

번호 선택 = '''

# print(prompt)

# [방법 1] 조건
# number = 0
# while number != 4:
#     print(prompt, end='')
#     number = int(input())

# [방법 2] 무한 루프
number = 0
while True:
    print(prompt, end='')
    number = int(input())
    if number == 4:
        break