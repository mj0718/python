# [방법 1]
# from urllib import request
# [방법 2]
# from urllib.request import urlretrieve
# [방법 3]
import urllib.request

import os

img_url = 'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMzAzMjhfNzMg%2FMDAxNjc5OTMyNDg4MTg1.d37-nxR-QfRGOyomvw3fzu_BRLRK2nqRQ5CXkNjMWBog.5xbFqp2T0OxjvqZSqVM2arMNV7m9HaYM1_oPWIJNtCQg.JPEG.luvmmk1111%2FIMG_1239.JPG&type=sc960_832'
file_path = os.path.join(os.path.dirname(__file__), 'cat4.jpg')

# [방법 1]
# request.urlretrieve(img_url, file_path)
# [방법 2]
# urlretrieve(img_url, file_path)
# [방법 3]
urllib.request.urlretrieve(img_url, file_path)

print('==이미지 다운로드 완료==')