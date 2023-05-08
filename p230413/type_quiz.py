# [문제]

number = [100, 200, 100, 500, 200, 600, 300]

# 1) 중복된 요소를 제거한 후, 오름차순 정렬
number = list(set(number))
number.sort()
print('정렬 후 number >>', number)

# 2) 요소 300 다음에 400 추가 (리스트로 나와야함)
number.insert(number.index(300)+1, 400)
print('추가 후 number >>', number)