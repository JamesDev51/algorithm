from fractions import Fraction

def solution(denum1, num1, denum2, num2):
    answer=str(Fraction(denum1,num1)+Fraction(denum2,num2))
    if "/" not in answer:
        answer+="/1"
    denum,num=list(map(int,answer.split("/")))
    
    for comDiv in range(min(denum,num),1,-1):
        if denum%comDiv==0 and num%comDiv==0:
            denum/=comDiv
            num/=comDiv
            break
    return [denum, num]