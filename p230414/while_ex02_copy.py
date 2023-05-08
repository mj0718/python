coffee = 3

while True:
    money = int(input('\n돈을 넣어주세요 >> '))

    if money == 300:
        print('커피를 줍니다.')
        coffee -= 1
    elif money > 300:
        print(f'잔돈 {money-300}원을 주고 커피를 줍니다.')
        coffee -= 1
    else:
        print('돈을 다시 돌려주고 커피는 주지 않습니다.')
    
    print(f'남은 커피는 {coffee}잔입니다.')

    if not coffee:
        print('=' * 40)
        print('커피가 다 떨어졌습니다. 판매 중지!')
        print('=' * 40)
        break

print('==프로그램 종료==')