'''
[문제] gugudan.txt 파일 마지막 위치에 리스트 변수 data 추가
- 한 라인에 요소 1개 쓰기
- with문으로 작성
'''
data = ['one', 'two', 'three']

#[방법 1]
# with open('D:\webservice\python\p230418\gugudan.txt', 'a') as gugudan: 
#     for element in data:
#         gugudan.write(element+'\n')

#[방법 2]
with open('D:\webservice\python\p230418\gugudan.txt', 'a') as gugudan:
    gugudan.writelines('\n'.join(data))
print('==프로그램 종료==')
