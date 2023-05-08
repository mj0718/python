'''
[문제] 웹 페이지 요청 후 파싱하시오
'''
from bs4 import BeautifulSoup
import requests

url = 'https://www.transfermarkt.com/spieler-statistik/wertvollstespieler/marktwertetop'

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}
html = requests.get(url, headers=headers)
html.status_code