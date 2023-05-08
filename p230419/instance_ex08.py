# 클래스 정의
class Fruit:
    # 생성자
    def __init__(self):
        print('생성자 실행됨')
    
    # 클래스 메서드
    @classmethod
    def create(cls):
        print('<< 클래스 메서드 실행 >>')
        return cls() # 객체 생성

class Banana(Fruit):
    # 생성자
    def __init__(self):
        print('바나나 생성자 실행됨')

    def like(self):
        print('바나나 좋아하나요?')

    def count(self, count):
        self.count = count
        print(f'바나나가 {self.count}개 있습니다.')

# 클래스 메서드 호출
fruit = Fruit.create()
banana = Banana.create()
banana.like()
banana.count(5)
print('banana 수 >>', banana.count)