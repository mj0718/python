even = [2, 4, 6, 8]

print('even[1] >>', even[1])

# 얕은 복사(shallow copy) : 주소만 복사
print('\n==얕은 복사(shallow copy): even_copy==')
even_copy = even
print('even >>', even)
print('even_copy >>', even_copy)
print('even에 저장된 주소 >>', id(even))
print('even_copy에 저장된 주소 >>', id(even_copy))

even_copy[1] = 10
print('[4 -> 10] even_copy >>', even_copy)
print('[4 -> 10] even >>', even)

# 깊은 복사(deep copy) : 리스트(데이터) 복사
print('\n==깊은 복사(deep copy): even_deep_copy==')
# 1) 함수
even_deep_copy = even.copy() 
print('even >>', even)
print('even_deep_copy : 함수 >>', even_deep_copy)
print('even에 저장된 주소 >>', id(even))
print('even_deep_copy에 저장된 주소 >>', id(even_deep_copy))

even_deep_copy[-1] = 9
print('[8 -> 9] even >>', even)
print('[8 -> 9] even_deep_copy : 함수 >>', even_deep_copy)

# 2) 슬라이싱
even_slicing = even[:]
print('even >>', even)
print('even_slicing >>', even_slicing)
print('even에 저장된 주소 >>', id(even))
print('even_slicing에 저장된 주소 >>', id(even_slicing))