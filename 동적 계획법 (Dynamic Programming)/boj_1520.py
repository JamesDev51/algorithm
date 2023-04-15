import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**7)

def go(y,x):
    if dp[y][x]!=-1:return dp[y][x]
    dp[y][x]=0
    for dy,dx in zip([-1,0,1,0],[0,1,0,-1]):
        ny,nx=y+dy,x+dx
        if 0<=ny<n and 0<=nx<m and mat[y][x]<mat[ny][nx]:
            dp[y][x]+=go(ny,nx)
    return dp[y][x]

if __name__=="__main__":
    n,m=map(int,input().split())
    mat=[list(map(int,input().split())) for _ in range(n)]
    dp=[[-1]*m for _ in range(n)];dp[0][0]=1
    print(go(n-1,m-1))
    