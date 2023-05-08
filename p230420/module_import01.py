# [방법 1] ===========================
# import 모듈명
# import 패키지명.모듈명
# ====================================

# import module
import pack.module

# 전역변수 value 접근
print('value >>', pack.module.value)

# show() 함수 호출
pack.module.show()

# 인스턴스 생성
ic = pack.module.Increment()
ic.showNumber(7)

print(dir(pack.module))