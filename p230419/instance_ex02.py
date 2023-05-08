'''
[클래스 변수]
- 객체 생성과 상관없음

                    선언 위치       접근 형태           할당 시기
인스턴스 변수       메서드 내       self.변수명         메서드 실행
클래스 변수         클래스 내       클래스명.변수명     클래스가 메모리 load될 때
'''

# 클래스 정의
class Person:
    # 클래스 변수
    count = 1

    # 생성자
    # def __init__(self):
    #     print('생성자 실행됨')
    #     self.count = 1
    #     print(f'{self.count}번 사람 생성')
    #     self.count += 1

    def __init__(self):
        print('생성자 실행됨')
        print(f'{Person.count}번 사람 생성')
        Person.count += 1

# 인스턴스 생성
print('count >>', Person.count)
p1 = Person()
p2 = Person()
print('count >>', Person.count)