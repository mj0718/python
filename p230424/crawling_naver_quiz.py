'''
[문제]
naver 경제 탭에서 우측의 분야별 주요뉴스 타이틀을 추출하여 news.txt 파일에 쓰시오.
- 모드 : 추가 쓰기
'''
from bs4 import BeautifulSoup
import urllib.request as request
import os
import requests
from datetime import datetime

url = 'https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=101'


# [방법 1] 거절될 때 user-agent로 웹사이트라고 속여서 접근
headers = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}
html = requests.get(url, headers=headers)
# print(html.status_code)  #상태(HTTP 응답) 코드

# [방법 2]
# html = request.urlopen(url).read()

soup = BeautifulSoup(html.content, 'html.parser')
# print(soup)

# news = soup.find('div', class_='classfy sd').find_all('a', class_='nclicks(rig.secteco)')
news = soup.find('div', class_='classfy sd').find_all('a')

path = os.path.join(os.path.dirname(__file__), 'news.txt')
with open(path, 'a', encoding='UTF-8') as naver_news:
    naver_news.write(f'\n기록일시 : {datetime.now()}\n')
    for idx, title in enumerate(news, 1):
        print(f'{idx}. {title.text}\n')