# [방법 2] =========================================
# from 모듈명 import 클래스명,함수명,변수명
# from 패키지.모듈명 import 클래스명,함수명,변수명
# from 패키지명 import 모듈명
# ==================================================

# from module import value #이렇게도 작성 가능
# from module import show

# from module import value, show, Increment

# from module import * # 모듈의 모든 것을 읽어옴
# --------------------------------------------------

# from pack.module import value, show, Increment

from pack import module

# 전역변수 접근
print('value >>', module.value)

# show() 함수 호출
module.show()

# 인스턴스 생성
ic = module.Increment()
ic.showNumber(5)