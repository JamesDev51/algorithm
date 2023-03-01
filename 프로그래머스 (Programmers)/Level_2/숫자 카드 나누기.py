from math import gcd
def solution(arrayA, arrayB):
    answer = 0
    gcd_a=arrayA[0]
    for i in range(1,len(arrayA)):gcd_a=gcd(gcd_a,arrayA[i])

    gcd_b=arrayB[0]
    for i in range(1,len(arrayB)):gcd_b=gcd(gcd_b,arrayB[i])
    
    if gcd_a>1:
        flag=True
        for b in arrayB:
            if b%gcd_a==0:flag=False;break
        if flag:answer=gcd_a
    
    if gcd_b>1:
        flag=True
        for a in arrayA:
            if a%gcd_b==0:flag=False;break
        if flag:answer=max(answer,gcd_b)
    
    
    return answer