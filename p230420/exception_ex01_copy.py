'''
[예외처리]
try:
    예외 발생 가능한 명령어
except:
    예외 발생 시 실행할 명령어
else:
    예외가 발생하지 않았을 때, 실행할 명령어
finally:
    예외 발생 여부와 상관없이, 마지막에 실행할 명령어

- try, except는 필수 else, finally는 선택사항
- 순서 맞춰서 써야 함
'''
n1, n2 = eval(input('정수 2개 입력...'))

try:
    result1 = n1 // n2
    result2 = n1 % n2
    print('몫 :', result1)
    print('나머지 :', result2)
except:
    print('분모가 0으로 계산 불능')    
finally:
    print('--예외처리 구문 종료--')

print('==프로그램 종료==')