'''
[클래스] 멤버
- 변수 : 인스턴스 변수, 클래스 변수
- 메서드 : 인스턴스 메서드, 클래스 메서드, 정적(static) 메서드

                            접근
인스턴스 메서드         [내부] self.메서드명()
                        [외부] 참조변수.메서드명()
                        [외부] 클래스명.메서드명(주소)

클래스 메서드           [외부] 클래스명.메서드명()

정적 메서드             [외부] 클래스명.메서드명()

'''

# 클래스 정의
class Thing:
    # 클래스 변수
    totalCount = 0

    # 생성자
    def __init__(self):
        print('생성자 실행됨')
        # 인스턴스 변수
        self.name = '상품'
        self.count = 0
        self.showInfo() # 메서드 호출할 때 self가 있어야함
        Thing.totalCount += 1

    # 메서드
    def setName(self, name):
        # 인스턴스 변수
        self.name = name

    def setCount(self, count):
        # 인스턴스 변수
        self.count = count

    def showInfo(self):
        print(f'{self.name}이고, 개수는 {self.count}개 있습니다.')

    # def showTotalCount(self):
    #     print(f'전체 상품 개수는 {Thing.totalCount}개 입니다.')

    # 클래스 메서드
    @classmethod
    def showTotalCount(cls): # 주소가 아닌 타입이 오게 됨
        print('cls >>', cls)
        print(f'전체 상품 개수는 {Thing.totalCount}개 입니다.')

# 인스턴스 생성
phone = Thing()
# phone.setName('갤럭시')
# phone.setCount(5)
# phone.showInfo()
# phone.showTotalCount()
Thing.showTotalCount() # 주소를 안 넣어도 됨

pen = Thing()
# pen.showTotalCount()
Thing.showTotalCount()