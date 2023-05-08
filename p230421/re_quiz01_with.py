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


with open(file_path, 'r', encoding='UTF-8') as morrie:
    file = morrie.read()

# 2. 데이터 추출 : 교수가 포함된 문장
cp = re.compile('[\w+\s,]*교수[\w+\s]*[.]')
professor = cp.findall(morrie)

 # 3. 화면 출력
for idx, line in enumerate(professor, 1):
    print(f'{idx}. {line.lstrip()}')
        
