import sys
sys.stdin = open("input.text",  "rt")
import sys
from math import comb
input=sys.stdin.readline

def solve():
    p_sum=[0]*(n+1)
    for i in range(1,n+1): p_sum[i]=p_sum[i-1]+arr[i-1] #구간합 배열
    
    res=0
    for i in range(m):
        cnt=0
        for j in range(1,n+1):
            if p_sum[j]%m==i:
                cnt+=1
        res+=comb(cnt,2)
        if i==0: res+=cnt
    return res
            
if __name__=="__main__":
    n,m=map(int,input().split())
    arr=list(map(int,input().split()))
    print(solve())