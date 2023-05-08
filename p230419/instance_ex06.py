class Animal:
    def __init__(self):
        print('부모의 생성자 실행')
        print('self >>', self)
        print('self에 저장된 주소 >>', id(self))

class Dog(Animal):
    def __init__(self):
        super().__init__()
        print('\n자식의 생성자 실행')
        print('self >>', self)
        print('self에 저장된 주소 >>', id(self))

# 인스턴스 생성
s = Dog()