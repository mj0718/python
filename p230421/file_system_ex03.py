import os

# 경로 존재 여부 확인
print(os.path.exists(r'D:\test'))
print(os.path.exists('D:\day'))

if os.path.exists(r'd:\test'):
    open(r'd:\test\ex.txt', 'w')
    print('ex.txt 파일 생성 완료!')

print(os.path.exists(r'd:\test\ex.txt'))
print(os.path.exists(r'd:\test\cf.txt'))

# directory 생성
# [방법 1] 예외처리
# try:
#     os.mkdir('d:\okay')
#     print('okay 폴더 생성')
# except:
#     print('이미 존재하는 폴더입니다.')
# print('==프로그램 종료==')

# [방법 2] if문
okay_path = 'd:\okay'

if not os.path.exists(okay_path):
    os.mkdir(okay_path)
    print('okay 폴더 생성')

#os.mkdir('d:\hey\sub')

'''
                                기본값
옵션                        exist_ok=False      exist_ok=True
경로가 존재하지 않을 때         경로 생성           경로 생성
경로가 존재할 때                에러 발생           에러 발생X
'''
# 계층구조 폴더 생성
os.makedirs('d:\hey\sub', exist_ok=True)

# test 폴더 삭제
# 1) 파일 삭제
# os.remove(r'd:\test\ex.txt')
# print('ex.txt 파일 삭제 완료')

# 2) 폴더 삭제
# os.rmdir(r'd:\test')
# print('test 폴더 삭제 완료')


# okay 폴더 삭제    
# os.rmdir(r'd:\okay')
# os.removedirs(r'd:\okay\sub')
# print('okay 폴더 삭제 완료')

os.rmdir(r'd:\hey\sub')

# 쉘 유틸리티
import shutil

shutil.rmtree(r'd:\hey')
print('hey 폴더 삭제')

print('==프로그램 종료==')
