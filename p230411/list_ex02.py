## [인덱싱, 슬라이싱 2] #####################

data = [2, 3.5, [1, 3, 5], 'Hello']

print('리스트 변수 data 길이 >>', len(data))
print('data >>', data)

## 인덱싱
print('data[1] >>', data[1])
print('data[1] type >>', type(data[1]))
print('data[2] >>', data[2][-1])

## ex)
print([100, 200, 300][1])

## 슬라이싱
print('data[:2] >>', data[:2])
print('data[:2] type >>', type(data[:2]))