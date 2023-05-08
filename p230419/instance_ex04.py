# 클래스 정의
class Cat:
    # 생성자
    def __init__(self):
        print('생성자 실행됨')

    # 메서드
    def showInfo(self):
        print('나는 고양이다')

# 인스턴스 생성
print('==one==')
one = Cat()
one.showInfo()

print('==two==')
two = Cat
two.__init__(Cat())
two.showInfo()