'''
[읽기 함수]
readline()   readlines()   read()
한 라인         전체        전체
 str           list         str

[파일 읽기] 
1. open 함수 : 모드 - r
2. read 함수
3. close 함수
'''

# 1. open 함수
gugudan = open('D:\webservice\python\p230418\gugudan.txt', 'r')

# 2. 읽기 함수: read()
lines = gugudan.read()
print(lines)
print(type(lines))

# 3. close 함수
gugudan.close()