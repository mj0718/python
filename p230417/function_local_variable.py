num = 1   ## 전역변수

## 함수 정의 ===================
def increment():
    # var = 50
    # num = 100     ## 지역변수

    global num
    # num = num + 1
    # print('함수 내에서 num 출력 >>', num)

## 함수 호출 ===================
increment()

# print('[지역 변수] var >>', var)
print('[전역 변수] num >>', num)