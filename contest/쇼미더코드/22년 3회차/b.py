import sys
sys.stdin = open("input.text",  "rt")
import sys
from collections import deque
input=sys.stdin.readline


def bfs():
    while que:
        y,x=que.popleft()
        for dy,dx in zip([-1,0,1,0],[0,1,0,-1]):
            ny,nx=y+dy,x+dx
            ny%=n; nx%=m
            if not mat[ny][nx] and not ch[ny][nx]:
                ch[ny][nx]=1
                que.append((ny,nx))

def solve():
    answer=0
    for y in range(n):
        for x in range(m):
            if not ch[y][x] and not mat[y][x]:
                ch[y][x]=1
                que.append((y,x))
                bfs()
                answer+=1
    return answer
        
        
        
    

if __name__=="__main__":
    n,m=map(int,input().split())
    mat=[list(map(int,input().split())) for _ in range(n)]
    que=deque()
    ch=[[0]*m for _ in range(n)]
    print(solve())
