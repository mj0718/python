# [문제] 사은품을 추첨하여 고객님께 제공하려고 합니다
# 사은품은 랜덤으로 추첨하되, 꽝이 나오는 순간 더이상 추첨하지 않습니다.
import random

castLots = ['생수', '지갑', '꽝', '커피', '과자', '도서', '핸드폰', '노트북']
print('셔플 전 >>', castLots)
random.shuffle(castLots)
print('셔플 후 >>', castLots)

for idx, cast in enumerate(castLots, 1):
    if '꽝' == cast:
        print(f'{idx}번 꽝입니다!')
        break

    print(f'{idx}번 {cast} 당첨! 축하!!')