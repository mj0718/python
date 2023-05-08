## 함수 정의 ==============================
def student_score(**score):
    print(score, type(score))
    add = sum(score.values())
    print('총점 >>', add)
    print(f'평균 >> {add/len(score):.1f}') ## 소수 1자리 표시


## 함수 호출 ==============================
student_score(math=90, eng=99, kor=95)