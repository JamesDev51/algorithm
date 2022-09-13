import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(y,x):
    for dy,dx in zip([-1,0,1,0],[0,1,0,-1]):
        ny,nx=y+dy,x+dx
        if 0<=ny<n and 0<=nx<m and mat[ny][nx] and not ch[ny][nx]:
            ch[ny][nx]=1
            dfs(ny,nx)

def solve():
    cnt=0
    for y in range(n):
        for x in range(m):
            if not ch[y][x] and mat[y][x]:
                cnt+=1
                ch[y][x]=1
                dfs(y,x)
    return cnt
                
                
if __name__=="__main__":
    for _ in range(int(input())):
        m,n,k=map(int, input().split())
        mat=[[0]*m for _ in range(n)]
        ch=[[0]*m for _ in range(n)]
        for _ in range(k):
            x,y=map(int,input().split())
            mat[y][x]=1
        print(solve())