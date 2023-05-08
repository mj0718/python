'''
[문제] gugudan.txt 파일을 생성하여 2~9단을 쓰시오.
모드 - 덮어 쓰기
경로 - 상대 경로 -> 절대 경로
'''
# 1. open 함수 
file = open('D:\webservice\python\p230418\gugudan.txt', 'w') 

# 2. write 함수
for i in range(2, 10):
    for j in range(1, 10):
        file.write(f'{i} * {j} = {i * j}\n')
    file.write('\n')

# 3. close 함수
file.close()
print('==프로그램 종료==')