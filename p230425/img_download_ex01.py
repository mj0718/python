'''
[urllib] request 라이브러리
- urlopen() : 요청하면 메모리에 올려놓고 read()로 읽어옴
- urlretrive() : 요청하고 바로 파일에 저장해줌
'''

import urllib.request as request
import os

img_url = 'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMzAzMjhfMjk4%2FMDAxNjc5OTgwMzE5MjY0.vcnnquHAcxXvysGRn96Lxr37RDPb8XbrO6NMq5F36Ggg.jtlM4_J4S_CvvorPLjLEabS7LNwLJtODmiKBdZNr8pEg.PNG.firstcatsw%2F2%25BD%25C7%25B9%25D9.png&type=sc960_832'
file_path = os.path.join(os.path.dirname(__file__), 'cat.jpg')
# print(file_path)

# 1. 이미지 요청
request_img = request.urlopen(img_url).read()
# print(request_img)

# 2. open 함수
img = open(file_path, 'wb') # binary 파일을 만드는 것 (모드의 defalut는 text)

# 3. write 함수
img.write(request_img)

# 4. close 함수
img.close()

print('==이미지 다운로드 완료==')