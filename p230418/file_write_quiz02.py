'''
[문제] numberTwo.txt 파일을 생성하여 1~100를 파일에 쓰시오.
모드 - 추가 쓰기
경로 - 상대 경로
'''
# 1. open 함수 
file = open('numberTwo.txt', 'a', encoding='UTF-8') 

# 2. write 함수
for r in range(1, 101):
    file.write(f'{r:<3} ')
    if r % 10 == 0:
        file.write('\n') 

# 3. close 함수
file.close()
print('==프로그램 종료==')