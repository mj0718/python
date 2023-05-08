import pandas

url = 'https://finance.naver.com/'

table = pandas.read_html(url, encoding='cp949') # cp949 또는 euc-kr 둘다 가능
# print(table)
# print(type(table))
# print(len(table))
# print(table[1])

top = table[0]
print(top)
print(type(top))