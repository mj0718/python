# [방법 2] =========================================
# from 모듈명 import 클래스명,함수명,변수명
# from 패키지.모듈명 import 클래스명,함수명,변수명
# from 패키지명 import 모듈명
# from 패키지명 import 모듈명 as 별칭
# ==================================================

# from module import value #이렇게도 작성 가능
# from module import show

# from module import value, show, Increment

# from module import * # 모듈의 모든 것을 읽어옴
# --------------------------------------------------

# from pack.module import value, show, Increment

# from pack import module

from pack import module as md

# 전역변수 접근
print('value >>', md.value)

# show() 함수 호출
md.show()

# 인스턴스 생성
ic = md.Increment()
ic.showNumber(5)