import sys
sys.stdin = open("input.text",  "rt")
import sys
input=sys.stdin.readline

dy,dx=[-1,-1,-1],[-1,0,1]

def solution():
    costs=[[[float('inf')]*3 for _ in range(m)] for _ in range(n)]
    for x in range(m):
        for d in range(3):
            costs[0][x][d]=mat[0][x]
    for y in range(1,n):
        for x in range(m):
            for d1 in range(3):
                for d2 in range(3):
                    if d1==d2:continue
                    ny,nx=y+dy[d1],x+dx[d1]
                    if 0<=ny<n and 0<=nx<m:
                        costs[y][x][d1]=min(costs[y][x][d1],costs[ny][nx][d2]+mat[y][x])
    res=float('inf')
    for q in costs[-1]:res=min(res,min(q))
    return res

if __name__=="__main__":
    n,m=map(int, input().split())
    mat=[list(map(int, input().split())) for _ in range(n)]
    print(solution())