import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline


if __name__=="__main__":
    n,m,k=map(int,input().split())
    dp=[[0]*301 for _ in range(301)]
    graph=[[0]*(n+1) for _ in range(n+1)]
    for _ in range(k):
        a,b,c=map(int,input().split())
        if a>=b:continue
        graph[a][b]=max(graph[a][b],c)
    for e in range(2,n+1):
        dp[e][2]=max(dp[e][2],graph[1][e])
    for s in range(2,n):
        for e in range(s+1,n+1):
            taste=graph[s][e]
            if taste==0:continue
            for cnt in range(2,m): #최소 2개 ~ 
                if dp[s][cnt]==0:continue 
                dp[e][cnt+1]=max(dp[e][cnt+1],dp[s][cnt]+taste)
    print(max(dp[n]))