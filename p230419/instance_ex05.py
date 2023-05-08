'''
[상속]
- 다중 상속 허용

[문법]
class 부모클래스:
    멤버

class 자식클래스(부모클래스, 부모클래스):
    멤버

'''
class Sun:
    pass

class GrandParent:
    def rich(self):
        print('부자다')

class Parent:
    #클래스 변수
    money = 10000000

    def buy(self, money):
        Parent.money -= money
        print(f'남은 돈은 {Parent.money}원 입니다.')

class Child(Parent, GrandParent):
    # 메서드 오버라이딩
    # 상속관계에서 부모의 메서드 재정의 => 선언부는 그대로, 기능만 수정
    # 오버로딩은 불가능
    def buy(self, money):
        print(f'용돈 {money}원 주세요')

    # def buy(self):
    #     print(f'부모님 남은 돈 {Parent.money}원 입니다.')

# 인스턴스 생성
c = Child()
c.buy(200000)
# c.buy()
c.rich()

# 객체 소속
# isinstance(객체명, 클래스명)
num = 5
print('5는 int인가요? >>', isinstance(num, int))
print('객체 c는 Child와 관련있나요? >>', isinstance(c, Child))
print('객체 c는 Parent와 관련있나요? >>', isinstance(c, Parent))
print('객체 c는 Child, Parent와 관련있나요? >>', isinstance(c, (Child, Parent)))
print('객체 c는 Sun와 관련있나요? >>', isinstance(c, Sun))
print('객체 c는 Sun,Child와 관련있나요? >>', isinstance(c, (Sun, Child)))
