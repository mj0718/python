'''
[정규 표현식]
import re

변수 = re.compile('정규 표현식')
변수.함수명('문자열')

<< 함수 >>
match(): 문자열 첫 번째에서만 추출
search(): 문자열 전체를 기준으로 처음 검색된 데이터 추출
findall(): 일치하는 모든 데이터를 리스트로 리턴
finditer(): 일치하는 모든 데이터를 객체로 리턴


<< 메타문자 >>
- 메타문자: 원래 문자가 갖는 의미가 아닌 특별한 용도로 사용하는 문자
- . : 한 자리, 모든(\n 제외) 
- ^ : 시작하는

- 반복
    * : 0개 이상
    + : 1개 이상
    {n} : n개 
    {m,n} : m~n개 (m,n 포함 / , 사이에 공백 넣으면 안 됨)
    ? : 0~1개

- 문자 표현식
\w : [a-zA-Z0-9]
\W : [^a-zA-Z0-9] => ^는 부정을 의미 ex) 공백
\d : [0-9]
\D : [^0-9] => 숫자를 제외한 나머지
\s : [ \t\n\r\f\v] 
\S : [^ \t\n\r\f\v]


1) 단어 추출 : re.compile('[a-z]+')
2) 숫자 추출 : re.compile('[0-9]+')
3) 숫자 + 문자 추출 : re.compile('[0-9]+[a-z]+')
4) 문자 + 숫자 추출 : re.compile('[a-z]+[0-9]+')
5) 한글 추출 : re.compile('[가-힣]+')
'''
import re

data = '''abc mart food2
 10days aaa at   야호!!'''

cp = re.compile('^z')

# print('1) match :', cp.match(data))
# print('2) search :', cp.search(data))
print('3) findall :', cp.findall(data))
# print('4) finditer :', cp.finditer(data))

# for info in cp.finditer(data):
#     print(info)