# 논리형 
# 값 : True, False
# type : bool
# 함수 : bool(값) 

'''
(10진수)
정수 --> 논리
 0       False
0제외    True
'''

# 정수 -> 논리
print('정수 0의 논리값 >>', bool(0))
print('정수 1의 논리값 >>', bool(1))
print('정수 5의 논리값 >>', bool(5))
print('정수 -5의 논리값 >>', bool(-5))

# 문자열 -> 논리
print('문자열 Hi의 논리값 >>', bool('Hi'))
print('빈 문자열의 논리값 >>', bool(''))

# 리스트 -> 논리
print('리스트 [2, 4]의 논리값 >>', bool([2, 4]))
print('빈 리스트의 논리값 >>', bool([]))