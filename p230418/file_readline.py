'''
[파일 읽기] 
1. open 함수 : 모드 - r
2. readline 함수
3. close 함수
'''

# 1. open 함수
gugudan = open('D:\webservice\python\p230418\gugudan.txt', 'r')

# 2. 읽기 함수: readline()
while True:
    line = gugudan.readline() 
    # print('line type >>', type(line))
    if not line: # 빈 문자열일 때 종료
        break
    print(line, end='')

# 3. close 함수
gugudan.close()