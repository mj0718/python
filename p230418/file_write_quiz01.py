'''
[문제] number.txt 파일을 생성하여 1~100를 파일에 쓰시오.
모드 - 추가 쓰기
경로 - 상대 경로
1
2
3
4
...
100
'''

# 1. open 함수 
file = open('number.txt', 'a') 

# 2. write 함수
for r in range(1, 101):
    file.write(f'{r}\n') 

# 3. close 함수
file.close()
print('==프로그램 종료==')