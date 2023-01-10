from math import gcd

def solution(a, b):
    answer = 1
    now_gcd=gcd(a,b)
    a//=now_gcd
    b//=now_gcd
    while b>1:
        if b%5==0:b//=5
        elif b%2==0:b//=2
        else:answer=2;break
    return answer