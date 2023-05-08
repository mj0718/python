'''
[문법]
with open() as 변수:
    명령어
    명령어
'''
with open('D:\webservice\python\p230418\gugudan.txt', 'r') as gugudan:
    lines = gugudan.read()
    print(lines)
    print(type(lines))
print('==프로그램 종료==')