def hello():
    print('안녕')

# 함수명 출력 => 주소 출력됨
print('함수명 hello >>', hello)

# 변수에 함수 주소 저장
a = hello
a()