import os

# directory에 있는 목록
print(os.listdir())

# 현재 폴더에 있는 목록
current_path = os.path.dirname(__file__)
print(os.listdir(current_path))
