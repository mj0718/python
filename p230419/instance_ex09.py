# [문제] 해결하기 
# 클래스 정의
class Food:

    # 인스턴스 메서드
    def setSort(self, sort):
        # 인스턴스 변수
        self.sort = sort

    # 클래스 메서드
    @classmethod    # @: decorator
    def show(cls):
        print(f'음식 종류는 {cls.sort}입니다.')

# 인스턴스 생성
pizza = Food()
pizza.setSort('피자')
Food.show()
