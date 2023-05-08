# 문자열 함수

st = '  Hello  '

# 문자열 길이
print('st 길이 >>', len(st))

# 문자열에서 특정 문자의 개수
# 문법: 문자열.count(문자)
print('l의 개수 >>', st.count('l'))
print('He의 개수 >>', st.count('He'))

# 공백 제거
# 왼쪽 공백 제거: 문자열.lstrip()
# 오른쪽 공백 제거: 문자열.rstrip()
# 양쪽 공백 제거: 문자열.strip()
print('|' + st + '|')
print('|' + st.lstrip() + '|')
print('|' + st.rstrip() + '|')
print('|' + st.strip() + '|')

# 대소문자 변경
# 대문자 변경: 문자열.upper()
# 소문자 변경: 문자열.lower()
print('대문자로 변경 >>', st.upper())
print('소문자로 변경 >>', st.lower())

# 특정 문자의 인덱스(대소문자 구분)
# 문자열.find(찾고자 하는 문자열)
# 문자열.index(찾고자 하는 문자열)
print('e를 찾아라 1) >>', st.find('e'))
print('e를 찾아라 2) >>', st.index('e'))

print('a를 찾아라 1) >>', st.find('a'))
#print('a를 찾아라 2) >>', st.index('a'))

print('He를 찾아라 >>', st.find('He'))

# 특정 문자를 변경
# 문법: 문자열.replace('old', 'new')
print('ello를 i로 변경 >>', st.replace('ello', 'i'))

# 문자열 나누기
# 문법: 문자열.split(나누고자 하는 문자)
print('e를 기준으로 나누기 >>', st.split('e'))

# 특정 문자 추가
# 문법: '추가할 문자'.join(문자열 또는 여러값)
print('~ 추가 >>', '~'.join(st))