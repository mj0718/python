# 클래스 정의
class Animal:
    # 클래스 변수
    count = 1

    # 메서드
    def showInfo(self):
        self.age = 5
        print('저는 동물입니다.')

# 클래스 메서드 호출
Animal.showInfo(Animal())

# 인스턴스 생성
print('==one==')
one = Animal()
# one.showInfo()
Animal.showInfo(one)
print('인스턴스 변수 age >>', one.age)
print('클래스 변수 count >>', Animal.count)
print('클래스 변수 count >>', one.count)

print('\n==two==')
two = Animal()
two.showInfo()