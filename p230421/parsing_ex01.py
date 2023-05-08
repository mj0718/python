from bs4 import BeautifulSoup
html ='''
<html>
    <body>
        <h1>BeautifulSoup 연습합니다.</h1>
        <p>연습 중1</p>
        <p>연습 중2</p>
    </body>
<html>
'''
# print('html >>', html)
# print('html 타입 >>', type(html))

soup = BeautifulSoup(html, 'html.parser') # 계층구조로 분석
# print(soup)
# print(type(soup))
# print(soup.prettify())

# [h1 엘리먼트 추출]
print(soup.html.body.h1)
print(type(soup.html.body.h1))

# [h1 엘리먼트 content 추출]
print(soup.html.body.h1.text)
print(type(soup.html.body.h1.text)) #str

print(soup.html.body.h1.string) 
print(type(soup.html.body.h1.string)) #bs4.element.NavigableString

print(soup.html.body.h1.get_text())
print(type(soup.html.body.h1.get_text())) #str

print(soup.html.body.h1.getText()) # get_text의 주소가 저장되어 있으므로 같은 것임
print(type(soup.html.body.h1.getText())) #str

# [body 엘리먼트 content 추출]
print(soup.body)
print(soup.body.text) # enter 인식 때문에 한줄 띄어져있는 것임
print(soup.body.string) # 엘리먼트 추출을 못해서 None 출력됨
print(soup.body.get_text())
print(soup.body.getText())

# [h1에서 접근 시작] 
# 최상위 엘리먼트(노드) html에서 시작하지 않아도 됨
print(soup.h1)
print(soup.h1.text)

# [p 접근] 
# p가 여러 개 있으면 제일 처음 p만 추출됨
print(soup.p)

# [p 엘리먼트 추출]
p = soup.html.body.p
print('p :', p)

# [형제 엘리먼트에 접근]
p2 = p.next_sibling.next_sibling # enter 때문에 두번 해줘야 함
print('p2 :',p2)

h1 = p.previous_sibling.previous_sibling
print('h1 :', h1)

# [일부의 엘리먼트 추출]
body = soup.html.body
print('body =========')
print(body)
print('h1 추출 :', body.h1)