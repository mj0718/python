from bs4 import BeautifulSoup

html = '''
<html lang="en">
<body>
    <p id="wrap">
        <a class="website" id="naver" href="https://www.naver.com">NAVER</a>
        <a class="website" id="daum" href="https://www.daum.net">DAUM</a>
        <a class="website" id="google" href="https://www.google.com">GOOGLE</a>
    </p>
</body>
</html>
'''

soup = BeautifulSoup(html, 'html.parser')
# print(soup)

'''
[문법]
find(name, attrs, recursive, string, kwargs)
recursive: true(default) - 모든 자손 탐색
           false         - 직계 자손 탐색
'''
# 모든 a 추출
# 1. 태그 : 모든 a 엘리먼트 추출
a_all_01 = soup.find_all('a')
print('a_all_01 >>', a_all_01)
print('a_all_01 type >>', type(a_all_01))

# 2.1. 속성 : class가 website인 엘리먼트 추출
a_all_02 = soup.find_all(class_="website")
print('a_all_02 >>', a_all_02)

# 2.2 속성 : id 속성이 있는 a 엘리먼트 추출
a_all_03 = soup.find_all('a', id=True)
print('a_all_03 >>', a_all_03)
print('a_all_03 개수 >>', len(a_all_03))

# 2.3 속성 : 여러 개 지정
a_all_04 = soup.find_all(attrs={'class': 'website', 'id':'naver'})
print('a_all_04 >>', a_all_04)

# 3. 태그와 속성
a_all_05 = soup.find_all('a', class_='website')
print('a_all_05 >>', a_all_05)

# 4. content : content가 NAVER인 엘리먼트 추출
a_all_06 = soup.find_all('a', string='NAVER')
print('a_all_06 >>', a_all_06)

# a 하나만 추출
a_one_01 = soup.find('a')
print('a_one_01 >>', a_one_01)
print('a_one_01 type >>', type(a_one_01))

a_one_02 = soup.find(class_='website')
print('a_one_02 >>', a_one_02)

a_one_03 = soup.find('a', id=True)
print('a_one_03 >>', a_one_03)

p_one = soup.find(id=True)
print('p_one >>', p_one)
print('p_one type >>', type(p_one))
print(p_one.find_all('a'))