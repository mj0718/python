##########################
## [리스트 함수 1] 정렬 ##
##########################

number = [5, 1, 6, 3, 4, 2]

## 정렬(오름차순) =========================================
## 문법 : 리스트.sort()
print('정렬 전 number >>', number)
number.sort()
print('정렬 후 number >>', number)

alphabet = ['banana', 'apple', 'cat', 'egg', 'dog', 'car']
print('정렬 전 alphabet >>', alphabet)
alphabet.sort()
print('정렬 후 alphabet >>', alphabet)

hangul = ['다락방', '나비', '가방', '라디오', '나방']
print('정렬 전 hangul >>', hangul)
hangul.sort()
print('정렬 후 hangul >>', hangul)

## 정렬(역순) =============================================
## 문법 : 리스트.reverse()
print('역순 정렬 전 number >>', number)
number.reverse()
print('역순 정렬 후 number >>', number)

## 정렬(내림차순) =========================================
## 문법 : 리스트.sort(reverse=True)
number.sort(reverse=True)
print('내림차순 정렬 후 number >>', number)