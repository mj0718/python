# break
# - 반복문 내 사용
# - if문과 같이 사용
# - break가 실행되면, 반복문 탈출

num = 0

while num < 10:
    num += 1

    if num % 3 == 0:
        break
    print('num >>', num)

print('반복문 실행 후 num >>', num)
print('==프로그램 종료==')