'''
[문제]
D:\workspace\오늘날짜\현재시간.txt
D:\workspace\20230421\14571211111.txt

'''
import os
from datetime import datetime
from datetime import date

today = str(date.today()).replace('-','')

folder_path = 'D:/workspace/' + today 
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

file_name = str(datetime.now().time()).replace(':','').replace('.','')
os.chdir(folder_path)
# [방법 1]
file = open(file_name + '.txt', 'w')
file.close()

# [방법 2]
# with open(file_name + '.txt', 'w') as file:
#     pass

print('==작업 완료==')

# [내 답안]
# import os
# import datetime

# today = str(datetime.datetime.now().date()).replace('-','')
# time = str(datetime.datetime.now().time()).replace(':','').replace('.','')

# current_path = os.path.join('D:\workspace', today)
# os.makedirs(current_path, exist_ok=True)
# open(os.path.join(current_path, time) +'.txt', 'w')
# print('파일 생성 완료')