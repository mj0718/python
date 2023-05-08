## [함수 정의] ==============================
## [함수 정의 형태] 매개변수 있고, 리턴 있음
def add(n1, n2):
    result = n1 + n2
    return result
    # print('함수 실행 끝')


## [함수 호출] ==============================
result_value = add(3, 5)
print('add(3, 5) 호출 결과 >>', result_value, type(result_value))

print('add(1, 4) 호출 결과 >>', add(1, 4))