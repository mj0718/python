'''
[문제] gangnam.txt에서 연락처만 추출하여 파일에 쓰시오.
- 쓰기 파일 : phoneNumber.txt
- 추가 쓰기 모드

터미널 =========================
전체 연락처 개수 >> 50
연락처 추출 및 파일 기록 완료!!

phoneNumber.txt ================
1. 02-3452-1515
2. 070-4240-1116
이런 식으로 써있어야함
'''
import re

with open('D:\webservice\python\p230421\gangnam.txt', 'r') as gangnam:
    gangnam_read = gangnam.read()

cp = re.compile('\d{0,3}-?\d{0,4}-\d{4}')
phone_number = cp.findall(gangnam_read)

with open('D:\webservice\python\p230421\phoneNumber.txt', 'a') as phone:
    for idx, number in enumerate(phone_number, 1):
        phone.write(f'{idx}. {number}\n')
print('전체 연락처 개수 >>', len(phone_number))
print('연락처 추출 및 파일 기록 완료!!')