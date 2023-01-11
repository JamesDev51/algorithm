def solution(x):
    answer = True
    sum_of_each=0
    num=x
    while num:
        sum_of_each+=num%10
        num//=10
    answer=True if x%sum_of_each==0 else False
    return answer