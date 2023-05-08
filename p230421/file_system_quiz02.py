'''
[문제] chemical 폴더 내 모든 파일명 숫자만 뽑아서 chemical.txt 파일에 쓰기
'''
import os
import re
# 1. 지정된 경로에서 파일명 읽어오기
cur_path = os.path.join(os.path.dirname(__file__), 'chemical')
file_list = os.listdir(cur_path)

# 2. 리스트 -> 문자열
file_list_str = ''.join(file_list)

# 3. 파일명의 일부 추출
cp = re.compile('\d+-\d+-.')
file_name = cp.findall(file_list_str)

# 4. 쓰기 작업
write_path = os.path.join(os.path.dirname(__file__), 'chemical.txt')
with open(write_path, 'w') as chemical:
    for name in file_name:
        chemical.write(name + '\n')
print('==작업 완료==')

# 21라인이 없어서 추가 쓰기 시에는 바로 옆에서 써짐
# with open(write_path, 'w') as chemical:
#     chemical.write('\n'.join(file_name)) 

# [내 답안]
# import os
# import re

# data = os.listdir('D:\webservice\python\p230421\chemical')
# with open('D:\webservice\python\p230421\chemical.txt', 'a') as chemical:
#     cp = re.compile('\d+[-]+\d+[-]+\d+')
#     for che in data:
#         result = cp.findall(che)
#         for re in result:
#             chemical.write(re + '\n')