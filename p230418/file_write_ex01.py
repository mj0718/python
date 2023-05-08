'''
[파일 쓰기] 탐색기에 있는 파일의 최상위 경로로 만들어짐
1. open 함수 : 모드 - w(덮어쓰기), a(덧붙이기)
2. write 함수
3. close 함수
'''

# 1. open 함수 
file = open('new.txt', 'a') # 상대 주소 (찾는 위치와 생성 위치가 다름)
# print('file >>', file)

# 2. write 함수
file.write('\nhoho') # 줄바꿈은 직접 해야함

# 3. close 함수
file.close()
print('==프로그램 종료==')