'''
딕셔너리 : dict
- 여러 값을 묶어서 하나의 데이터 형태로 관리
- {key:value, 키:값, 키:값}
- 저장 순서가 보장되지 않음 => 인덱스 사용 불가능
- key를 통해 value 접근 가능
- key는 value를 구분하는 기준 => 중복 불가능
- value는 중복과 상관없음
'''

hong = {'name':'홍길동', 'age':35, 'address':'서울 서대문구'}
print('hong >>', hong)
print('hong type >>', type(hong))

print('hong 요소 수 >>', len(hong))

# 키를 통한 값 추출
print('이름 >>', hong['name'])
print('나이 >>', hong['age'])
# print(hong[0])

# 요소 추가
hong['phone'] ='010-1111-1111'
print('hong >>', hong)
print('hong 요소 수 >>', len(hong))

# 값 변경
hong['age']=100
print('hong >>', hong)

# 요소 삭제
del hong['address']
print('address 요소 삭제 후 >>', hong)

# 값 추출 : 함수
print('[get 함수] 연락처 >>', hong.get('phone'))
print('[key] 연락처 >>', hong['phone'])

print('[get 함수] 주소 >>', hong.get('address', '주소 없음')) #key가 없을 경우 보고자 하는 값 설정 가능
# print('[key] 주소 >>', hong['address'])

# 키만 추출
keys = hong.keys()
print('키만 추출 >>', keys)
print('keys type >>', type(keys))
# print('keys[0] >>', keys[0]) Error

keys_list = list(keys)
print('타입을 리스트로 변경 >>', keys_list)
print('keys_list type >>', type(keys_list ))
print('keys_list[0] >>', keys_list[0])

# 값만 추출
values = hong.values()
print('값만 추출 >>', values)

# 키와 값을 쌍으로 추출
items = hong.items()
print('키와 값을 쌍으로 추출 >>', items)

# in 연산자 
# [문법] 값 in 여러값 
print('name' in hong)
print('address' in hong)

#[문제] 홍길동 값 존재 여부 확인
print('홍길동 값이 있나요? >>', '홍길동' in hong.values())

# 요소 추가 : 함수
print(hong)

# 1) 요소 1개 추가
hong.update({'주소':'서울 강남구'})
print('주소 추가 후 >>', hong)

# 2) 요소 여러 개 추가
hong.update({'취미':'산책', '특기':'놀기'})
print('요소 여러 개 추가 후 >>', hong)

# 3) 존재하는 키 => 값 수정
hong.update({'age':500})
print('age update >>', hong)

# 모든 요소 삭제
hong.clear()
print('모든 요소 삭제 후 >>', hong)