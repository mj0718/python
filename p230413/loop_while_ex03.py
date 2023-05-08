# continue
# - 반복문 내 사용
# - if문과 같이 사용
# - continue가 실행되면, 조건검사 실행

num = 0

while num < 10:
    num += 1

    if num % 3 == 0:
        continue
    print('num >>', num)

print('반복문 실행 후 num >>', num)
print('==프로그램 종료==')