'''
[클래스] class
- 클래스는 자료형이다
- 멤버 : 변수(field), 메서드(method)
- 클래스명 : 대문자로 시작

[클래스] 멤버
- 변수 : 인스턴스 변수, 클래스 변수
- 메서드 : 인스턴스 메서드, 클래스 메서드, 정적(static) 메서드

========================================================
                            접근
인스턴스 메서드         [내부] self.메서드명()
                        [외부] 참조변수.메서드명()
                        [외부] 클래스명.메서드명(주소)

클래스 메서드           [외부] 클래스명.메서드명()

정적 메서드             [외부] 클래스명.메서드명()
========================================================

- [문법] 클래스 정의
class 클래스명:
    멤버 변수

    멤버 메서드

cf) 변수 종류
- 전역 변수
- 지역 변수 : 함수 내
-- << 클래스 내 >> --
- 인스턴스 변수 : 메서드가 실행되어야 만들어짐 
- 클래스 변수

- 생성자 
    * 객체 생성될 때 변수 초기화, 특정 매서드(기능) 자동 실행을 원할 시 생성자 사용
    * 1개만 정의 가능
    * 객체 생성될 때 무조건 실행
    * 생성자를 명시하지 않으면, 기본 생성자가 실행 
    -> 매개변수 없고, 기능 없음
    -> 형식상 실행
    * 생성자명 : __init__
'''
# 클래스 정의
class Student:
    # def __init__(self):
    #     print('매개변수 1개인 생성자 실행됨')

    # def __init__(self, name):
    #     print('매개변수 2개인 생성자 실행됨')
    #     self.name = name

    def __init__(self, name, age):
        print('매개변수 3개인 생성자 실행됨')
        self.name = name
        self.age = age

    def greeting(self):
        print('안녕하세요')
        # print('self에 저장된 주소 >>', self)

    def setName(self, name):
        self.name = name

    def showInfo(self):
        print('제 이름은 ' + self.name + '입니다.')
        print(f'나이는 {self.age}세 입니다.')

# 인스턴스(객체) 생성
print('==hong==')
hong = Student('홍길동', 29)
hong.greeting()
# print('hong에 저장된 주소 >>', hong)
# hong.setName('홍길동')
hong.showInfo()

print('\n==park==')
park = Student('박보검', 35)
park.greeting()
# print('park에 저장된 주소 >>', park)
# park.setName('박보검')
park.showInfo()
park.__init__('박보검2', 55)

print('\n==lee==')
# lee = Student()
