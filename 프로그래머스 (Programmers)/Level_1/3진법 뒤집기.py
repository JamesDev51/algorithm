def convert_3_and_revert(num):
    ret=''
    while num:
        ret=str(num%3)+ret
        num//=3
    return int(ret[::-1],3)

def solution(n):
    answer=convert_3_and_revert(n)
    return answer