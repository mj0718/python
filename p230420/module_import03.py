# [방법 3] ============================
# import 모듈명 as 별명
# import 패키지명.모듈명 as 별칭
# =====================================

# import module as md
import pack.module as md

# 전역변수 접근
print('value >>', md.value)

# show() 함수 호출
md.show()

# 인스턴스 생성
ic = md.Increment()
ic.showNumber(6)