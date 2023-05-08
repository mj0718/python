'''
[문제] 네이버 증권 페이지에서 국내증시 탭의 테이블을 stock.csv 파일에 저장하시오. 
- 모드 : 추가 쓰기
'''
import pandas as pd
import os

url = 'https://finance.naver.com/sise/lastsearch2.naver'

table = pd.read_html(url, encoding='euc-kr')[1]

path = os.path.join(os.path.dirname(__file__), 'stock.csv')
table.to_csv(path, index=False, header=False, mode='a') # index를 없애기