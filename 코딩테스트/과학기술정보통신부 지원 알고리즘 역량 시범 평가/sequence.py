# import sys
# sys.stdin = open("input.text",  "rt")

import sys
input=sys.stdin.readline


def solve():
    ret=1
    if n==3: return 1
    for i in range(n-3):
        ret+= 4*pow(3,i)
    return ret
MOD=1000000007

n=int(input())

    
res=(pow(3,n)-solve())%MOD
print(res)