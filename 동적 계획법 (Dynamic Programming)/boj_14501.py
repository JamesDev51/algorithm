import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline


if __name__=="__main__":
    n=int(input())
    infos=[list(map(int,input().split())) for _ in range(n)]

    dp=[0]*(n+2)
    for i in range(1,n+1):
        dp[i]=max(dp[i-1],dp[i])
        t,p=infos[i-1]
        if i+t<=n+1:
            dp[i+t]=max(dp[i+t],dp[i]+p)
    print(max(dp))
    