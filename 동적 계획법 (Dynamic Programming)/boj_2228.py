import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

from copy import deepcopy

if __name__=="__main__":
    n,m=map(int,input().split())
    arr=[int(input()) for _ in range(n)]
    for i in range(1,n):arr[i]+=arr[i-1]
    arr.insert(0,0)
    dp=[[0]*(m+1) for _ in range(n+1)]
    for i in range(1,m+1):dp[0][i]=float('-inf')
    
    for i in range(1,n+1): #숫자 인덱스
        for j in range(1,m+1): #인덱스
            dp[i][j]=dp[i-1][j]
            for k in range(1,i+1):
                if k>=2:
                    dp[i][j] = max(dp[i][j], dp[k-2][j-1] + arr[i] - arr[k-1])
                elif k==1 and j==1:
                    dp[i][j] = max(dp[i][j], arr[i]);
    print(dp[n][m])