'''
[문제] morrie.txt에서 교수가 들어간 문장만 추출하여 출력하시오.

총 6개

1. 문장
2. 문장 
이런 식으로 출력
'''
import os, re

# 파일 읽어오기
path = os.path.dirname(__file__)   
file_path = os.path.join(path, 'morrie.txt')

# 1.1 open 함수
file = open(file_path, 'r', encoding='UTF-8')

# 1.2 읽기 함수
morrie = file.read()
# print(morrie)

# 1.3 close 함수
file.close()

# 2. 데이터 추출 : 교수가 포함된 문장
cp = re.compile('[\w+\s,]*교수[\w+\s]*[.]')
professor = cp.findall(morrie)

# 3. 화면 출력
for idx, line in enumerate(professor, 1):
    print(f'{idx}. {line.lstrip()}')
 
# [내 답안]
# with open('D:\webservice\python\p230421\morrie.txt', 'r', encoding='UTF-8') as morrie:
#     content = morrie.read()

#     cp = re.compile('[^. ]+[^.]+교수+[^.]*[.]')

#     for idx, value in enumerate(cp.findall(content), 1):
#         print(f'{idx}. {value}')