from bs4 import BeautifulSoup

html = '''
<html>
    <body>
        <div id="wrap">
            <h1>공지</h1>
            <h2>과목</h2>
            <ul class="lec">
                <li>파이썬 기초1</li>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
                <li>파이썬 기초2</li>                                                     
                <li>머신러닝</li>
            </ul>
            <h2>강의 일정</h2>
            <h2>교재 목록</h2>
        </div>
    </body>
</html>
'''

soup = BeautifulSoup(html, 'html.parser')
# print(soup)

# 모든 h2 추출
h2_all_01 = soup.select('html > body > div > h2')
print('모든 h2 추출 1)', h2_all_01)
print(type(h2_all_01))

h2_all_02 = soup.select('body h2')
print('모든 h2 추출 2)', h2_all_02)
print(type(h2_all_02))

h2_all_03 = soup.select('div > h2')
print('모든 h2 추출 3)', h2_all_03)
print(type(h2_all_03))

h2_all_04 = soup.select('#wrap > h2')
print('모든 h2 추출 4)', h2_all_04)
print(type(h2_all_04))

'''
[문제] 아래와 같이 content만 추출하시오.
과목
강의 일정
교재 목록
'''
for h2 in h2_all_04:
    print(h2.text)

print(h2_all_04[0])
print(h2_all_04[0:2])

# h2 하나 추출
h2_one_01 = soup.select_one('div > h2')
print('h2 하나 추출 1)>>',h2_one_01)
print(type(h2_one_01))

h2_one_02 = soup.select_one('div h2:nth-of-type(1)') 
print('h2 하나 추출 2)>>',h2_one_02)

h2_one_03 = soup.select_one('div h2:nth-of-type(2)')
print('h2 하나 추출 3)>>',h2_one_03)

'''
[문제] 아래와 같이 content만 추출하시오.
파이썬 기초1
파이썬 기초2
머신러닝
'''
ul_select_one = soup.select_one('ul.lec')
print(ul_select_one.text)