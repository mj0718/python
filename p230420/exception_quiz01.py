# [문제] 문자열 요소 중 정수만 출력 (예외처리 사용)
list_value = ['100', 'good', '5', '250', 'hi', '500']
list_number = []

for value in list_value:
    try:
        int(value)
        list_number.append(value)
    except:
        pass # 예외 회피 

print('list_number >>', list_number)