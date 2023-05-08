##########################
## [리스트 함수 2]      ##
##########################

data = ['one', 'two', 'three', 'four']

## 특정 요소의 인덱스 ==============================
## 문법 : 리스트.index(요소)
print('요소 two의 인덱스 >>', data.index('two'))
# print('요소 ten의 인덱스 >>', data.index('ten'))

## 요소 추가 : 마지막 위치 =========================
## 문법 : 리스트.append(값)
print('five 추가 전 요소 수 >>', len(data))
data.append('five')
print('five 추가 후 요소 수 >>', len(data))
print('five 추가 후 data >>', data)

## 요소 추가 : 특정 위치 =========================
## 문법 : 리스트.insert(인덱스, 값)
data.insert(1, '하나')
print('하나 추가 후 data >>', data)

## 요소 추가 : 여러 요소 추가 ====================
## 문법 : 리스트.extend(리스트)
even = [2, 4]
# data.extend(even)
## [문제] + 연산자를 이용하여 extend와 같은 결과가 출력되도록 하시오.
# data = data + even
data += even
print('리스트 변수 even 요소 추가 후 data >>', data)

## 요소 삭제  ======================================
## 문법 : 리스트.remove(요소)
element = data.remove('하나')
print('하나 삭제 후 data >>', data)
print('삭제된 요소 : remove 함수 리턴값 >>', element)

## 요소 삭제  ======================================
## 문법 : 리스트.pop()
## 문법 : 리스트.pop(인덱스)
element = data.pop()
print('마지막 요소 삭제 후 data >>', data)
print('삭제된 요소 >>', element)

data.pop(1)
print('인덱스 1의 요소 삭제 후 data >>', data)

## 요소 삭제  ======================================
## 문법 : del 리스트[인덱스]
del data[0]
print('인덱스 0의 요소 삭제 후 data >>', data)

del data[-2:]
print('인덱스 -2에서 끝까지의 요소 삭제 후 data >>', data)

## 특정 요소 개수  =================================
## 문법 : 리스트.count(요소)
four_count = data.count('four')
print('요소 four 개수 >>', four_count)