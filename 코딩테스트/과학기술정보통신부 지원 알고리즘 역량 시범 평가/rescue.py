import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline
from collections import deque

if __name__=="__main__":
    n=int(input())
    p=list(map(int,input().split()))
    p.insert(0,0)
    
    dp=[0]*(n+1)
    dp[1]=p[1]
    dp[2]=p[2]
    
    for i in range(3,n+1):
        dp[i]=max(dp[i-1],dp[i-2])+p[i]
    print(dp)
    print(dp[n])