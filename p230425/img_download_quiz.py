'''
[문제] 네이버 날씨 페이지에서 4개의 이미지 다운로드 하시오.
- 저장 위치: d:\img\오늘날짜
- 파일명: 시분초.jpg
'''
from bs4 import BeautifulSoup
import urllib.request as request
import requests
import os
from datetime import datetime, date

# 1. 웹페이지 요청
url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%82%A0%EC%94%A8'

html = requests.get(url)

# 2. 파싱
soup = BeautifulSoup(html.text, 'html.parser')

# 3. 엘리먼트 추출
imgs = soup.find_all('img', class_='thumb api_get api_img')
# print(imgs)
# print(imgs[0]['data-lazysrc'])

# 4. 이미지 저장 폴더 생성
today = str(date.today()).replace('-','')
folder_path = f'D:/img/{today}/'

os.makedirs(folder_path, exist_ok=True)

# 5. 이미지 다운로드
for img in imgs:
    file_name = str(datetime.now().time()).replace(':','').replace('.','') 
    save_path = folder_path + file_name + '.jpg'
    request.urlretrieve(img['data-lazysrc'], save_path)
print('==이미지 다운로드 완료==')