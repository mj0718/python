lt = [2, 4, 6]    ## mutable    : 변경 가능한~
num = 1           ## immutable  : 변경 불가능한~

def change():
    lt[1] = 5
    print('[함수 내] lt >>', lt)

    global num
    num = num + 1
    print('[함수 내] num >>', num)

change()

print('lt >>', lt)