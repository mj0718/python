# [문제 1] 인수로 정수 2개 입력하여 호출하면, 덧셈, 뺄셈, 곱셈, 나눗셈의 식과 계산된 값을 출력하는 함수 정의
def four_rules(num1, num2):
    print(f'{num1} + {num2} = {num1 + num2}')
    print(f'{num1} - {num2} = {num1 - num2}')
    print(f'{num1} * {num2} = {num1 * num2}')
    print(f'{num1} / {num2} = {num1 // num2}')

four_rules(7, 2)

# [문제 2] 인수로 정수 1개 입력하여 호출하면, 입력된 인수의 값만큼 별이 반복하여 출력되는 함수 정의
def star_count(num):
    print('*' * num)

star_count(7)

# [문제 3] 인수로 정수 2개 입력하여 호출하면, 두 수의 누적합을 출력하는 함수 정의
def accumulator(num1, num2):
    # [방법 1] if문
    # if num1 > num2:
    #     max, min = num1, num2 
    # else:
    #     max, min = num2, num1

    # [방법 2] 조건연산자
    max, min = (num1, num2) if num1 > num2 else (num2, num1)
    print('누적 합 :', sum(range(min, max+1)))
    
accumulator(1, 10)
accumulator(10, 1)

# [문제 4] 리스트를 인수로 positive함수 호출하면, 양수 값만 출력하는 함수 정의
def positive(args):
    result = []
    for ar in args:
        if ar > 0:
           result.append(ar)
    return result

positiveValue = positive([1, -2, 3, -4, 5])
print(positiveValue)

# [문제 5] 인수로 받은 값을 딕셔너리 student에 저장하는 함수 정의
def addInfo(**args):
    student = {'info' : {}}
    # student['info'] = args
    student['info'].update(args)
    print(student)

# addInfo(name='kim', gender='female', score=2.34)

# [문제 5-1] 인수로 받은 값을 딕셔너리 student에 저장하는 함수 정의 
# key가 1씩 자동으로 증가하고 인수가 값으로 들어가는 형태로 

def addInfo(**args):
    student = {'info' : {}}
    count = len(student['info']) + 1
    student['info'][count] = args
    count += 1
    print(student)

addInfo(name='kim', gender='female', score=2.34)
addInfo(name='hong', gender='male', score=3.5)