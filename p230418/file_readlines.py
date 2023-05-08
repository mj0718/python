'''
[파일 읽기] 
1. open 함수 : 모드 - r
2. readlines 함수
3. close 함수
'''

# 1. open 함수
gugudan = open('D:\webservice\python\p230418\gugudan.txt', 'r')

# 2. 읽기 함수: readlines()
lines = gugudan.readlines()
# print(lines)
# print(type(lines))
# print('요소 수 >>', len(lines))

for i in lines:
    print(i, end='')

# 3. close 함수
gugudan.close()