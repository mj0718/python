""" 
리스트
- 여러 값을 묶어서 하나의 데이터 형태로 관리
- [요소1, 요소2, 요소3] 
- 인덱스로 요소에 접근 (0부터 시작)
- 저장 순서 보장
 """

num = 5

data=[2, 4, 6]
print('data >>', data)
print('data type >>', type(data))

# 인덱싱: 하나의 요소 추출
print('첫 번째 요소 추출 >>', data[0])
print('마지막 요소 추출 1) >>', data[2])
print('마지막 요소 추출 2) >>', data[-1])

# 슬라이싱: 연속된 여러 개 요소 추출 
print('첫 번째 ~ 두 번째 요소 추출 >>', data[0:2])
print('두 번째 ~ 마지막 요소 추출 >>', data[1:])
print('data[:2] >>', data[:2])
print('data[:] >>', data[:])

data = [2, 4, 6, 8, 10]
print('data[1:] >>', data[1:])
print('data[1::2] >>', data[1::2])
print('data[::2] >>', data[::2])
print('data[::-1] >>', data[::-1])