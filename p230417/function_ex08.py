## 기본값 설정
## 함수 정의 ==============================
def default(a, b=0, c=-1):
    print(f'a: {a}, b: {b}, c: {c}')

## 함수 호출 ==============================
default(2, 4, 6)
default(1, 3)
# default(8) 
default(c=3, a=1)