import os

print(__file__)

# 경로(directory)만 추출
print(os.path.dirname(__file__))

current_path = os.path.dirname(__file__)
print(current_path + '\\'+'gugudan.txt')

# 경로에 알아서 \가 들어가짐 (결과는 위 코드와 동일)
print(os.path.join(current_path, 'gugudan.txt'))

print(os.path.join(current_path, 'new_folder'))

# 상위(현재) 경로 (파일이 속한 폴더의 상위 폴더 경로)
print(os.getcwd())

# 경로 변경
os.chdir(r'D:\test') #r을 쓰면 경로 그대로 인식
print(os.getcwd())