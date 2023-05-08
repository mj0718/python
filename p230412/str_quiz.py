# [문제] 
# 문자열 내 공백 제거 후 가운데 3자리 숫자 추출
numbering = ' a23 -456 - bc321'

# 공백 제거
numbering_copy = numbering.replace(' ','')
print('numbering >>', numbering)
print('numbering_copy >>', numbering_copy)

# 가운데 3자리 추출
print(numbering_copy.split('-')[1])