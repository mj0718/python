'''
[문제] daum의 경제 탭에서 오늘의 연재 타이틀을 화면에 출력하시오.

'''
from bs4 import BeautifulSoup
import requests
import urllib.request as request

url = 'https://news.daum.net/economic#1'

# [방법 1]
html = requests.get(url).content

# [방법 2]
# html = request.urlopen(url).read()

soup = BeautifulSoup(html, 'html.parser')

title = soup.find('ul', class_='list_todayseries').find_all('a', class_='link_txt')
for idx, news_title in enumerate(title, 1):
    print(f'{idx}. {news_title.text}')