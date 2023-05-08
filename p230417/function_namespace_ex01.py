## global namespace
num = 5         ## 전역 변수
print('globals() >>', globals())

def change():
    ## local namespace
    # num = 100   ## 지역 변수
    print('함수 내 globals() >>', globals()) #함수의 네임스페이스를 볼 수 있음
    print('함수 내 locals() >>', locals()) #실행하는 공간에 namespace를 출력
    print('함수 내 num >>', num)

change()

print('num >>', num)